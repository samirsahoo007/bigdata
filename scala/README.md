# Install scala by manually downloading it

Download the binaries from the official website(https://www.scala-lang.org/download/)

```
tar -zxvf scala-2.12.8.tgz
```

Add the following to ~/.bash_profile or ~/.bashrc

```
export SCALA_HOME="/Users/USERNAME/scala-2.12.6"
export PATH=$PATH:$SCALA_HOME/bin
```

```
source ~/.bash_profile
```

# How to Install Scala and Apache Spark on MacOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
xcode-select --install
brew cask install java
brew install scala
brew install apache-spark
```

# Setup environment variables
Setup SCALA_HOME
```
export SCALA_HOME="/usr/local/Cellar/scala/2.13.5"
export PATH=$PATH:$SCALA_HOME/libexec/bin/:$SCALA_HOME/libexec/lib/
```

Setup SPARK_HOME
```
export SPARK_HOME=/usr/local/Cellar/apache-spark/2.0.1/libexec
export PYTHONPATH=/usr/local/Cellar/apache-spark/2.0.1/libexec/python/:$PYTHONPATH$
```

