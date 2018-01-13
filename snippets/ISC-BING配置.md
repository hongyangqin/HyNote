
# 使用 BIND 作为本地的DNS缓存

1. 下载BIND
2. 解压
3. 以管理员身份运行
  ![1]
4. 输入密码，但是不知道有什么用
  ![2]
5. 在 C:\Program Files\ISC BIND 9\etc 创建 named.conf
  ![3]
  ```
	options {        
		directory "C:\Program Files\ISC BIND 9\etc";
		listen-on { 127.0.0.1; ::1; };
		forwarders {
			222.201.130.30;
			114.114.114.114;
			8.8.8.8;
			2001:4860:4860::8888;
			2001:4860:4860::8844;
	  };
	};

	logging {
		channel default_file {
			file "default.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel general_file {
			file "general.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel database_file {
			file "database.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel security_file {
			file "security.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel config_file {
			file "config.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel resolver_file {
			file "resolver.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel xfer-in_file {
			file "xfer-in.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel xfer-out_file {
			file "xfer-out.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel notify_file {
			file "notify.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel client_file {
			file "client.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel unmatched_file {
			file "unmatched.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel queries_file {
			file "queries.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel network_file {
			file "network.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel update_file {
			file "update.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel dispatch_file {
			file "dispatch.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel dnssec_file {
			file "dnssec.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};
		channel lame-servers_file {
			file "lame-servers.log" versions 3 size 5m;
			severity dynamic;
			print-time yes;
		};

		category default { default_file; };
		category general { general_file; };
		category database { database_file; };
		category security { security_file; };
		category config { config_file; };
		category resolver { resolver_file; };
		category xfer-in { xfer-in_file; };
		category xfer-out { xfer-out_file; };
		category notify { notify_file; };
		category client { client_file; };
		category unmatched { unmatched_file; };
		category queries { queries_file; };
		category network { network_file; };
		category update { update_file; };
		category dispatch { dispatch_file; };
		category dnssec { dnssec_file; };
		category lame-servers { lame-servers_file; };
	};
  ```
6. 打开系统服务，启动 ISC BIND 服务
  ![4]
7. 设置电脑的DNS
  ![5]
8. BIND 的 缓存只存放在内存中，放弃

[1]:assets/ISC-BING配置-c6529.png
[2]:assets/ISC-BING配置-faa56.png
[3]:assets/ISC-BING配置-c544a.png
[4]:assets/ISC-BING配置-eaa06.png
[5]:assets/ISC-BING配置-ce18c.png
