# Selenium

[![CI - Ruby](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-ruby.yml/badge.svg)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-ruby.yml)
[![CI - Python](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-python.yml/badge.svg)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-python.yml)
[![CI - JavaScript](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-javascript.yml/badge.svg)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-javascript.yml)
[![CI - Java](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-java.yml/badge.svg)](https://github.com/SeleniumHQ/selenium/actions/workflows/ci-java.yml)

<a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>

Selenium is an umbrella project encapsulating a variety of tools and
libraries enabling web browser automation. Selenium specifically
provides an infrastructure for the [W3C WebDriver specification](https://w3c.github.io/webdriver/)
— a platform and language-neutral coding interface compatible with all
major web browsers.

The project is made possible by volunteer contributors who've
generously donated thousands of hours in code development and upkeep.

Selenium's source code is made available under the [Apache 2.0 license](https://github.com/SeleniumHQ/selenium/blob/trunk/LICENSE).

## Documentation

Narrative documentation:

* [User Manual](https://selenium.dev/documentation/)

API documentation:

* [C#](https://seleniumhq.github.io/selenium/docs/api/dotnet/)
* [JavaScript](https://seleniumhq.github.io/selenium/docs/api/javascript/)
* [Java](https://seleniumhq.github.io/selenium/docs/api/java/index.html)
* [Python](https://seleniumhq.github.io/selenium/docs/api/py/)
* [Ruby](https://seleniumhq.github.io/selenium/docs/api/rb/)

## Pull Requests

Please read [CONTRIBUTING.md](https://github.com/SeleniumHQ/selenium/blob/trunk/CONTRIBUTING.md)
before submitting your pull requests.

## Requirements

* [Bazelisk](https://github.com/bazelbuild/bazelisk), a Bazel wrapper that automatically downloads
  the version of Bazel specified in `.bazelversion` file and transparently passes through all
  command-line arguments to the real Bazel binary.
* The latest version of the [Java 11 OpenJDK](https://openjdk.java.net/)
* `java` and `jar` on the `$PATH` (make sure you use `java` executable from JDK but not JRE).
  * To test this, try running the command `javac`. This command won't exist if you only have the JRE
  installed. If you're met with a list of command-line options, you're referencing the JDK properly.
* [Python 3.7+](https://www.python.org/downloads/) and `python` on the `PATH`
* [Ruby 3+](https://www.ruby-lang.org/en/documentation/installation/) and `ruby` on the `PATH`
* [The tox automation project](http://tox.readthedocs.org/) for Python: `pip install tox`
* macOS users:
  * Install the latest version of Xcode including the command-line tools. This command should work `xcode-select --install` 
  * Apple Silicon Macs should add `build --host_platform=//:rosetta` to their `.bazelrc.local` file. We are working
  to make sure this isn't required in the long run.
* Windows users:
  *  Latest version of [Visual Studio](https://www.visualstudio.com/) with command line tools and build tools installed
  * `BAZEL_VS` environment variable should point to the location of the build tools,
     e.g. `C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools`
  * `BAZEL_VC` environment variable should point to the location of the command line tools,
     e.g. `C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC`
  * `BAZEL_VC_FULL_VERSION` environment variable should contain the version of the installed command line tools,
     e.g. `14.27.29110`
  * A detailed setup guide can be seen on Jim Evan's [post](http://jimevansmusic.blogspot.com/2020/04/setting-up-windows-development.html)
  * If the Jim's blog instructions were followed, also make sure `C:\tools\msys65\usr\bin` is on the `PATH`.

### Internet Explorer Driver

If you plan to compile the
[IE driver](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver),
you also need:

* [Visual Studio 2008](https://www.visualstudio.com/)
* 32 and 64-bit cross compilers

The build will work on any platform, but the tests for IE will be
skipped silently if you are not building on Windows.

## Building

### Contribute with GitPod

GitPod provides a ready to use environment to develop.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/SeleniumHQ/selenium)

To configure and use your local machine, keep reading.

### Bazel

[Bazel](https://bazel.build/) was built by the fine folks at Google. Bazel manages dependency
downloads, generates the Selenium binaries, executes tests, and does it all rather quickly.

More detailed instructions for getting Bazel running are below, but if you can successfully get
the java and javascript folders to build without errors, you should be confident that you have the
correct binaries on your system.

### Before Building

Ensure that you have Firefox installed and the latest
[`geckodriver`](https://github.com/mozilla/geckodriver/releases/) on your `$PATH`.
You may have to update this from time to time.

### Common Build Targets

#### Java

<details>
<summary>Click to see Java Build Steps</summary>

To build the most commonly-used modules of Selenium from source, execute this command from the root
project folder:

```sh
bazel build java/...
```

If you want to test you can run then you can do so by running the following command

```sh
bazel test //java/... --test_size_filters=small,medium,large --test_tag_filters=<browser>
```

The `test_size_filters` argument takes small, medium, large. Small are akin to unit tests,
medium is akin to integration tests, and large is akin to end to end tests.

The `test_tag_filters` allow us to pass in browser names and a few different tags that we can
find in the code base.
  
To build the Grid deployment jar, run this command:

```sh
bazel build grid
```

The log will show where the output jar is located.
  
</details>

#### JavaScript
<details>
<summary>Click to see JavaScript Build Steps</summary>

If you want to build all the JavaScript code you can run:

```sh
bazel build javascript/...
```

To build the NodeJS bindings you will need to run:

```sh
bazel build //javascript/node/selenium-webdriver
```

To run the tests run:

```sh
bazel test //javascript/node/selenium-webdriver:tests
```

You can pass in the environment variable `SELENIUM_BROWSER` with the name of the browser.

To publish to NPM run:

```sh
bazel run //javascript/node/selenium-webdriver:selenium-webdriver.publish
```
</details>

#### Python
<details>
<summary>Click to see Python Build Steps</summary>

If you want to build the python bindings run:

```sh
bazel build //py:selenium
```

To run the tests run:

```sh
bazel test //py:test-<browsername>
```

If you add `--//common:pin_browsers` it will download the browsers and drivers for you to use.
  
To install locally run:
  
```sh
bazel build //py:selenium-wheel
pip install bazel-bin/py/selenium-*.whl
```

To publish run:

```sh
bazel build //py:selenium-wheel
twine upload bazel-bin/py/selenium-*.whl
```
</details>

####  Ruby
<details>
<summary>Click to see Ruby Build Steps</summary>

To build the Ruby code run:

```sh
bazel build //rb/...
```
</details>

####  .NET
<details>
<summary>Click to see .NET Build Steps</summary>

To build the .NET code run:

```sh
bazel build //dotnet/...
```

Also
```sh
bazel build //dotnet/test/common:chrome
```
  
</details>


### Build Details

Bazel files are called BUILD.bazel, and the order the modules are built is determined 
by the build system. If you want to build an individual module (assuming all dependent 
modules have previously been built), try the following:

```sh
bazel test javascript/atoms:test
```

In this case, `javascript/atoms` is the module directory,
`test` is a target in that directory's `BUILD.bazel` file.

As you see *build targets* scroll past in the log,
you may want to run them individually.

### Build Output

`bazel` makes a top-level group of directories with the  `bazel-` prefix on each directory.


### Common Tasks (Bazel)

To build the bulk of the Selenium binaries from source, run the
following command from the root folder:

```sh
bazel build java/... javascript/...
```

To run tests within a particular area of the project, use the "test" command, followed
by the folder or target. Tests are tagged with "small", "medium", or "large", and can be filtered
with the `--test_size_filters` option:

```sh
bazel test --test_size_filters=small,medium java/...
```

Bazel's "test" command will run *all* tests in the package, including integration tests. Expect
the ```test java/...``` to launch browsers and consume a considerable amount of time and resources.

To bump the versions of the pinned browsers to their latest stable versions:

```sh
bazel run scripts:pinned_browsers > temp.bzl && mv temp.bzl common/repositories.bzl
```

### Editing Code

Most of the team use either Intellij IDEA or VS.Code for their day-to-day editing. If you're
working in IntelliJ, then we highly recommend installing the [Bazel IJ
plugin](https://plugins.jetbrains.com/plugin/8609-bazel) which is documented on
[its own site](https://plugins.jetbrains.com/plugin/8609-bazel).

If you do use IntelliJ and the Bazel plugin, there is a project view checked into the tree
in [scripts/ij.bazelproject](scripts/ij.bazelproject) which will make it easier to get up
running, and editing code :)


## Tour

The codebase is generally segmented around the languages used to
write the component. Selenium makes extensive use of JavaScript, so
let's start there. First of all, start the development server:

```sh
bazel run debug-server
```

Now, navigate to
[http://localhost:2310/javascript](http://localhost:2310/javascript).
You'll find the contents of the `javascript/` directory being shown.
We use the [Closure Library](https://developers.google.com/closure/library/) 
for developing much of the JavaScript, so now navigate to
[http://localhost:2310/javascript/atoms/test](http://localhost:2310/javascript/atoms/test).

The tests in this directory are normal HTML files with names ending
with `_test.html`.  Click on one to load the page and run the test.

## Help with `go`

More general, but basic, help for `go`…

```sh
./go --help
```

`go` is a wrapper around
[Rake](http://rake.rubyforge.org/), so you can use the standard
commands such as `rake -T` to get more information about available
targets.

## Maven _per se_

Selenium is not built with Maven. It is built with `bazel`, 
though that is invoked with `go` as outlined above,
so you do not have to learn too much about that.

That said, it is possible to relatively quickly build Selenium pieces
for Maven to use. You are only really going to want to do this when
you are testing the cutting-edge of Selenium development (which we
welcome) against your application. Here is the quickest way to build
and deploy into your local maven repository (`~/.m2/repository`), while
skipping Selenium's own tests.

```sh
./go maven-install
```

The maven jars should now be in your local `~/.m2/repository`.

## Updating Java dependencies

The coordinates (_groupId_:_artifactId_:_version_) of the Java dependencies
are defined in the file [maven_deps.bzl](https://github.com/SeleniumHQ/selenium/blob/trunk/java/maven_deps.bzl).
The process to modify these dependencies is the following:

1. (Optional) If we want to detect the dependencies which are not updated,
   we can use the following command for automatic discovery:

```sh
bazel run @maven//:outdated
```

2. Modify [maven_deps.bzl](https://github.com/SeleniumHQ/selenium/blob/trunk/java/maven_deps.bzl).
   For instance, we can bump the version of a given artifact detected in the step before.

3. Repin dependencies. This process is required to update the file [maven_install.json](https://github.com/SeleniumHQ/selenium/blob/trunk/java/maven_install.json),
   which is used to manage the Maven dependencies tree (see [rules_jvm_external](https://github.com/bazelbuild/rules_jvm_external) for further details). The command to carry out this step is the following:

```sh
REPIN=1 bazel run @unpinned_maven//:pin
```

4. (Optional) If we use IntelliJ with the Bazel plugin, we need to synchronize
   our project. To that aim, we click on _Bazel_ &rarr; _Sync_ &rarr; _Sync Project
   with BUILD Files_.


## Running browser tests on Linux

In order to run Browser tests, you first need to install the browser-specific drivers,
such as [`geckodriver`](https://github.com/mozilla/geckodriver/releases),
[`chromedriver`](https://chromedriver.chromium.org/), or
[`edgedriver`](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
These need to be on your `PATH`.

By default, Bazel runs these tests in your current X-server UI. If you prefer, you can
alternatively run them in a virtual or nested X-server.

1. Run the X server `Xvfb :99` or `Xnest :99`
2. Run a window manager, for example, `DISPLAY=:99 jwm`
3. Run the tests you are interested in:
```sh
bazel test --test_env=DISPLAY=:99 //java/... --test_tag_filters=chrome
```

An easy way to run tests in a virtual X-server is to use Bazel's `--run_under`
functionality:
```
bazel test --run_under="xvfb-run -a" //java/... --test_tag_filters=chrome
```

## Bazel Installation/Troubleshooting

### Selenium Build Docker Image

If you're finding it hard to set up a development environment using bazel
and you have access to Docker, then you can build a Docker image suitable
for building and testing Selenium in from the Dockerfile in the 
[dev image](scripts/dev-image/Dockerfile) directory.

### MacOS

#### bazelisk

Bazelisk is a Mac-friendly launcher for Bazel. To install, follow these steps:

```sh
brew tap bazelbuild/tap && \
brew uninstall bazel; \
brew install bazelbuild/tap/bazelisk
```

#### Xcode

If you're getting errors that mention Xcode, you'll need to install the command-line tools.

Bazel for Mac requires some additional steps to configure properly. First things first: use
the Bazelisk project (courtesy of philwo), a pure golang implementation of Bazel. In order to
install Bazelisk, first verify that your Xcode will cooperate: execute the following command:

`xcode-select -p`

If the value is `/Applications/Xcode.app/Contents/Developer/`, you can proceed with bazelisk
installation. If, however, the return value is `/Library/Developer/CommandLineTools/`, you'll
need to redirect the Xcode system to the correct value.

```
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer/
sudo xcodebuild -license
```

The first command will prompt you for a password. The second step requires you to read a new Xcode
license, and then accept it by typing "agree".

(Thanks to [this thread](https://github.com/bazelbuild/bazel/issues/4314) for these steps)


<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>
