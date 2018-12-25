# Install Python, Virtualenv, Virtualenvwrapper on macOS

## Python
### Installation via Pyenv method

pyenv is a Python version manager that can manage and install different versions of Python. Works very much like rbenv for Ruby. First, we must install pyenv using Homebrew:

```
$ brew install pyenv
```

To upgrade pyenv in the future, use upgrade instead of install. After installing, add pyenv init to your shell to enable shims and autocompletion (use .zshrc if you're using zsh).

```
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

Restart your shell so the path changes take effect.

```
$ exec $SHELL
```

You can now begin using pyenv. To list the all available versions of Python, including Anaconda, Jython, PyPy and Stackless, use:

```
$ pyenv install --list
```

Then install the desired versions:

```
$ pyenv install 2.7.12
$ pyenv install 3.5.2
```

Use the global command to set global version(s) of Python to be used in all shells. For example, if you prefer 2.7.12 over 3.5.2:

```
$ pyenv global 2.7.12 3.5.2
$ pyenv rehash
```

The leading version takes priority. All installed Python versions can be located in ~/.pyenv/versions. Alternatively, you can run:

```
$ pyenv versions
  system (set by /Users/your_account/.pyenv/version)
* 2.7.12
* 3.5.2
```

This shows an asterisk * next to the currently active version.

## Virtualenv
### Installation

To install virtualenv run:

```
$ pip install virtualenv
```

## Virtualenvwrapper
### Installation

Installing with Homebrew (for OS X users)
Mac OS X users can install pyenv-virtualenvwrapper with the Homebrew package manager.

This is recommended method of installation if you installed pyenv with Homebrew.

```
$ brew install pyenv-virtualenvwrapper
```

Append to `~/.bash_profile` or `~/.zshrc`:

```
export PYENV_VIRTUALENVWRAPPER_PREFER_PYVENV="true"
export WORKON_HOME=$HOME/.virtualenvs
pyenv virtualenvwrapper_lazy
```

Reload the shell:

```
$ source ~/.bash_profile
```