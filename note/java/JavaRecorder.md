<!--toc-->

- [JavaRecorder](#javarecorder)
	- [程序原理](#程序原理)
		- [录音](#录音)
		- [播放](#播放)
		- [保存文件](#保存文件)
		- [打开文件](#打开文件)
	- [代码](#代码)
		- [获取 `DataLine` 对象](#获取-dataline-对象)
			- [设置格式信息](#设置格式信息)
			- [设置 'DataLine' 的信息](#设置-dataline-的信息)
			- [AudioSystem 获取](#audiosystem-获取)
		- [录音](#录音-1)
		- [播放](#播放-1)
			- [从内存中播放](#从内存中播放)
			- [从文件中播放](#从文件中播放)
		- [保存音频到文件中](#保存音频到文件中)
	- [遇到的问题](#遇到的问题)
		- [保存到文件之后，使用打开的方式播放文件，播放出来的不是正确的声音,噪声很大](#保存到文件之后使用打开的方式播放文件播放出来的不是正确的声音噪声很大)
	- [参考](#参考)

<!-- tocstop -->
# JavaRecorder
java写的简单录音程序

## 程序原理
![2]
### 录音
1. 通过 `AudioSystem` 获取 `TargetDataLine`
2. 对 `TargetDataLine`  进行读取，可以获得从麦克风中输入的信息

### 播放
1. 通过 `AudioSystem` 获取 `SourceDataLine`
2.  对 `SourceDataLine`  进行写入，可以把声音输出到播放设备

### 保存文件
```{java}
public static int write(AudioInputStream stream,
                        AudioFileFormat.Type fileType,
                        OutputStream out)
                 throws IOException
```

### 打开文件
```{java}
public static AudioInputStream getAudioInputStream(File file)
                                            throws UnsupportedAudioFileException,
                                                   IOException
```

## 代码
注意：下面的代码都没有把流关闭

### 获取 `DataLine` 对象

#### 设置格式信息
```{java}
public static AudioFormat getAudioFormat()
{  
        AudioFormat.Encoding encoding = AudioFormat.Encoding.PCM_SIGNED ;  
        float rate = 8000f;  
        int sampleSize = 16;  
        boolean bigEndian = true;  
        int channels = 1;  
        return new AudioFormat(encoding, rate, sampleSize, channels,  
                (sampleSize / 8) * channels, rate, bigEndian);      
}

AudioFormat af = getAudioFormat();  
```

#### 设置 'DataLine' 的信息
```{java}
DataLine.Info dataLineInfo = new DataLine.Info(TargetDataLine.class,af);
DataLine.Info dataLineInfo = new DataLine.Info(SourceDataLine.class, af);
```

#### AudioSystem 获取
```{java}
TargetDataLine td = (TargetDataLine)(AudioSystem.getLine(dataLineInfo));
SourceDataLine sd = (SourceDataLine) AudioSystem.getLine(dataLineInfo);
```

### 录音
从 **麦克风(TargetDataLine)**  中读取声音信息 存放到 **baos** 中
```{java}
ByteArrayOutputStream baos;
class Recorder implements Runnable {
  @Override
  public void run() {
    try {

      AudioFormat af = getAudioFormat();
      DataLine.Info info = new DataLine.Info(TargetDataLine.class, af);
      TargetDataLine td = (TargetDataLine) (AudioSystem.getLine(info));

      td.open(af);
      td.start();

      byte bts[] = new byte[10000];
      baos = new ByteArrayOutputStream();
      while (flg) {
        int cnt = td.read(bts, 0, bts.length);
        if (cnt > 0) {
          baos.write(bts, 0, cnt);
        }
      }

    } catch (Exception e) {
      e.printStackTrace();
    }
  }

}
```

### 播放
#### 从内存中播放
读取 **baos** 的数据进行播放
```{java}
ByteArrayOutputStream baos;
class Play implements Runnable {
  public void run() {			
    try {
      byte audioData[] = baos.toByteArray();

      AudioFormat af = getAudioFormat();
      DataLine.Info dataLineInfo = new DataLine.Info(SourceDataLine.class, af);
      SourceDataLine sd = (SourceDataLine) AudioSystem.getLine(dataLineInfo);

      sd.open(af);
      sd.start();
      sd.write(audioData, 0, audioData.length);

    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

#### 从文件中播放
```{java}
void open() throws Exception {
  File file = new File("C:\\Users\\qhy\\Desktop\\1479806522134.mp3");
  AudioInputStream ais = AudioSystem.getAudioInputStream(file);

  AudioFormat af = AudioSystem.getAudioFileFormat(file).getFormat();
  DataLine.Info dataLineInfo = new DataLine.Info(SourceDataLine.class, af);
  SourceDataLine sd = (SourceDataLine) AudioSystem.getLine(dataLineInfo);

  sd.open();
  sd.start();

  byte buf[] = new byte[0xFF];
  int len;
  while ((len = ais.read(buf, 0, buf.length)) != -1) {
    sd.write(buf, 0, len);
  }

}
```

### 保存音频到文件中
```{java}
void save() {
		AudioFormat af = getAudioFormat();
		byte audioData[] = baos.toByteArray();
		ByteArrayInputStream bais = new ByteArrayInputStream(audioData);
		AudioInputStream ais = new AudioInputStream(bais, af, audioData.length / af.getFrameSize());
		File file = null;
		try {
			File filePath = new File("C:\\Users\\qhy\\Desktop");
			file = new File(filePath.getPath() + "/" + System.currentTimeMillis() + ".mp3");
			AudioSystem.write(ais, AudioFileFormat.Type.WAVE, file);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
```

## 遇到的问题
### 保存到文件之后，使用打开的方式播放文件，播放出来的不是正确的声音,噪声很大
1. 首先，使用其他播放器播放这个mp3文件，得到的录音和录制的时候是一样的，说明文件没问题，猜测可能是读取的问题
2. 可能是读取的时候，文件的格式不对
    通过输出保存时候的格式信息，和读取到的文件的格式信息比较，发现猜测正确
    ![1]


## 参考
[JavaRecorder](https://github.com/285571052/JavaRecorder)
[Java实现音频播放--JavaSound API编写音频处理程序](http://tech.163.com/tm/030531/030531_95896.html)
[java实现一个录音播放的功能](http://blog.csdn.net/computer_liuyun/article/details/16923809)


[1]:assets/JavaRecorder-ab891.png
[2]:assets/JavaRecorder-71d0d.png
