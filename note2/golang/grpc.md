# 错误处理

## 错误模型

google介绍了一个比较通用的错误模型

```
package google.rpc;

// The `Status` type defines a logical error model that is suitable for
// different programming environments, including REST APIs and RPC APIs.
message Status {
  // A simple error code that can be easily handled by the client. The
  // actual error code is defined by `google.rpc.Code`.
  int32 code = 1;

  // A developer-facing human-readable error message in English. It should
  // both explain the error and offer an actionable resolution to it.
  string message = 2;

  // Additional error information that the client code can use to handle
  // the error, such as retry info or a help link.
  repeated google.protobuf.Any details = 3;
}
```

1. https://cloud.google.com/apis/design/errors#error_model

## 错误代码

grpc预定义了一些错误代码, 可直接使用: https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto


## 错误详情

同错误代码, grpc内置了一些错误详情给用户使用: https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto

## 错误处理

### 重试错误

不是所有的错误都是无脑重试的, 可以通过503/429等进行细化配置


```
客户端可能使用指数退避算法重试 503 UNAVAILABLE 错误。 除非另有说明，否则最小延迟应为 1 秒。 除非另有说明，否则默认重试重复应当仅一次。

对于 429 RESOURCE_EXHAUSTED 错误，客户端可能会在更高层级以最少 30 秒的延迟重试。此类重试仅对长时间运行的后台作业有用。

对于所有其他错误，重试请求可能并不适用。首先确保您的请求具有幂等性，并查看 google.rpc.RetryInfo 以获取指导。
```

### 错误透传问题

理论上错误不应该透传出去, 但如果是用户上传你的代码自身有问题, 则还是需要一定透传错误的方法。


```
如果您的 API 服务依赖于其他服务，则不应盲目地将这些服务的错误传播到您的客户端。在翻译错误时，我们建议执行以下操作：

隐藏实现详细信息和机密信息。
调整负责该错误的一方。例如，从另一个服务接收 INVALID_ARGUMENT 错误的服务器应该将 INTERNAL 传播给它自己的调用者。
```

## 参考
1. https://github.com/avinassh/grpc-errors
2. https://grpc.io/docs/guides/error/