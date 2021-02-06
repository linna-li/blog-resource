---
title: "超入門個人用Python Note"
author: "linna.li"
tags: ["Python"]
categories: ["note"]
date: 2020-01-18
---

## BackGround

>Recently, there is a new 後輩 joined my team who is very good at Python, so i think i got a good chance to start learning python. ^ ^

## What i learned
_Before_:

Only know there is a language called python

_After_:

But it has many "friends?" 

**Python2**,  **Python3**-> 2 python version  

**pyenv** -> a tool that is used to change which version 

**pip3**, **pip** -> pip3 is used to download dependency for python2, pip is for python2

**virtualenv**(knew from my 後輩)->a tool used to make Python env, so i will also use this but not pipenv

**pipenv**-> pyenv + pip + virtualenv



## Let's try something

Before: 

```md
➜  ~ which python
/usr/local/bin/python
➜  ~ python -V
Python 2.7.13
➜  ~ python
Python 2.7.13 (default, Jun 22 2017, 17:48:16)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
➜  ~ python3
zsh: command not found: python3
➜  ~ pip -V
pip 9.0.1 from /usr/local/lib/python2.7/site-packages (python 2.7)
➜  ~ pip3 -V
zsh: command not found: pip3
➜  ~ pyenv -l
zsh: command not found: pyenv
➜  ~ pipenv -V
zsh: command not found: pipenv
➜  ~ virtualenv -V
zsh: command not found: virtualenv
```

So now i only have python2(pip inside), no python3, pip3, virtualenv, pipenv.

My senior recommend use pyenv to control, so i will install python3

### Install pyenv

```md
// insall pyenv
➜  ~ brew install pyenv
➜  ~ pyenv versions (check the python version i can use)
* system (set by /Users/lilinna/.pyenv/version)
// Try install different versions
➜  ~ pyenv install -v 3.5.5
➜  ~ pyenv versions
* system (set by /Users/lilinna/.pyenv/version)
  3.5.5
// I have python3 now! Let's try, need run pyenv rehash when we install or uninstall
// not sure what this doing, google said create shims.(python maintains shims in that directory to match every Python Command across every installed version pf Python)
➜  ~ pyenv rehash
➜  ~ pyenv global 3.5.5
// But
➜  ~ python3 -V
zsh: command not found: python3
➜  ~ python -V
Python 2.7.13
// Need to set PATH !
➜  ~ echo 'export PATH="/Users/lilinna/.pyenv/bin:$PATH"' >> ~/.zshrc
➜  ~ echo -e 'if command -v pyenv 1>/dev/null 2>&1;then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc
➜  ~ python -V
Python 3.5.5
➜  ~ pip -V
pip 9.0.1 from /Users/lilinna/.pyenv/versions/3.5.5/lib/python3.5/site-packages (python 3.5)
➜  ~ pip3 -V
pip 9.0.1 from /Users/lilinna/.pyenv/versions/3.5.5/lib/python3.5/site-packages (python 3.5)
// But python2 still can be used.
➜  ~ python2 -V
Python 2.7.13
➜  ~ python3 -V
Python 3.5.5
// try install another python2
➜  ~ pyenv install -v 2.7.14
➜  ~ which python2
/usr/local/bin/python2
➜  ~ pyenv rehash
➜  ~ which python2
/Users/lilinna/.pyenv/shims/python2
➜  ~ python2 -V
pyenv: python2: command not found
The `python2' command exists in these Python versions:
  2.7.14
// so python2 not work because i am using 3.5.5 and there is no python2 inside. Need to do
➜  pyenv global 2.7.14
➜  python -V
Python 2.7.14
➜  python2 -V
Python 2.7.14
➜  ~ pip -V
pip 9.0.1 from /Users/lilinna/.pyenv/versions/2.7.14/lib/python2.7/site-packages (python 2.7)
```

## How to use

```md
➜  ~ python
Python 2.7.14 (default, Jan 18 2020, 16:10:59)
[GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.12)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Lsvirtualenv

Need to try requirements.txt

```md
➜  ~ pip install virtualenv
➜  ~ cd project
➜  project mkdir python_sandbox
➜  python_sandbox virtualenv first
Using base prefix '/Users/lilinna/.pyenv/versions/3.5.5'
➜  ~ virtualenv -p /usr/bin/python2.7 first
Running virtualenv with interpreter /usr/bin/python2.7
➜  ~ source first/bin/activate
(first) ➜  ~ python -V
Python 2.7.10
(first) ➜  ~ deactivate
➜  ~ virtualenv -p /Users/lilinna/.pyenv/shims/python3.5 first
➜  ~ source first/bin/activate
(first) ➜  ~ python -V
Python 3.5.5
(first) ➜  ~ deactivate

// virtualenvwrapper is a helper of virtualenv
➜  ~ pip install virtualenvwrapper
Add "export WORKON_HOME=/Users/lilinna/project/python_sandbox" into zshrc
➜  source ~/.zshrc
➜  source /Users/lilinna/.pyenv/versions/3.5.5/bin/virtualenvwrapper.sh
➜  mkvirtualenv second
(second) ➜  ~ python -V
Python 3.5.5
(second) ➜  deactivate
➜  ~ mkvirtualenv --python=/usr/bin/python2.7 django
(django) ➜  ~ python -V
Python 2.7.10
➜  ~ workon
django
first
second
➜  ~ rmvirtualenv django
Removing django...
```

## pipenv

TBD

pyenv + pip + virtualenv, so more aggregated things ? 

```md
pip3 install pipenv
pipenv run XXX
```

## Others

If you are not use pyenv, you can have python2 and python3 at the same time,

and you can change your python to use python2 or python3

```md
vim .bash_profile
//when we run python, should actually run python3, so python is another name of python3 
alias python='python3'   
source .bash_profile
```

but change version is not easy. 

I had some problem like 

Failed when i want to install 3.5.0 https://github.com/pyenv/pyenv/issues/950

```md
brew install pyenv-virtualenv
CFLAGS=-I/usr/include/openssl LDFLAGS=-L/usr/lib pyenv install -v 3.5.3
install -v 3.5.0
python3 -V
```

# Practice

I used python to wirte a simple script, to send request by curl http3, to calculate the average response time.

```md
import subprocess
def main():
    http3 = ['curl', '--http3', '-s', 'https://quic.rocks:4433/','-o','output', '-w' ,'%{time_total}']
    http2 = ['curl', '--http2', '-s', 'https://quic.rocks/','-o','output', '-w' ,'%{time_total}']
    http2Result = 0.0
    http3Result = 0.0
    for num in range(0,50):
       out_bytes1 = subprocess.check_output(http2)
       out_text1 = out_bytes1.decode('utf-8')
       http2Result = http2Result + float(out_text1) 
       out_bytes2 = subprocess.check_output(http3)
       out_text2 = out_bytes2.decode('utf-8')
       http3Result = http3Result + float(out_text2)    
    else:
       print ("http3Result:")
       print  (http3Result/50)
       print ("http2Result:")
       print  (http2Result/50)
    exit(0)
if __name__ == '__main__':
    main()
​```