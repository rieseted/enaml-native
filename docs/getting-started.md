
### Overview

This article covers how to install enaml-native, it's dependencies, and create your first app.

1. Install the [system](#system-dependencies) dependencies
2. Install the [app](#app-dependencies) SDKs and tools (Android and/or iOS dependencies)
3. Install [enaml-native](#installing-enaml-native)
4. Create a [new project](#creating-and-run-a-new-project)


Instructions for each are below. Please feel free to suggest changes or ask for help if you run into issues.

### System dependencies

The toolchain now provides precompiled packages that can be installed and used from Windows, 
Ubuntu and OSX by using the `conda` package manager.   

The preferred method is to install the `conda` package manager is by installing `miniconda` 
from [conda.io/miniconda.html](https://conda.io/miniconda.html).

> Note: [conda-mobile](https://github.com/codelv/conda-mobile) is a new build system that 
enaml-native now uses which completely replaces python-for-android and kivy-ios with a uniform
system for both Android and iOS.  

Once installed you should be able to run `conda --version` from the command line to see which
version you have and make sure it was installed correctly.

Next we install the Android and iOS SDK's.

### App dependencies

##### Android SDK

1. Download [android studio](https://developer.android.com/studio/index.html)
2. Once done, open it and go to `Tools->Android->SDK Manager` from the menu
3. Under the `SDK Platforms` tab, select `Android 7.1.1` (or latest)
4. and under the `SDK Tools` tab, select `Android SDK Build-Tools 26` (or latest), `Android Emulator`, `Android SDK Platform-Tools`, and `Android SDK Tools` (they should be selected by default)
5. Now click apply and let everything download (takes a LONG time)


#### iOS 

iOS apps can only be built with a mac or macbook running OSX.

You must install `xcode` from the App Store before continuing.


### Installing the enaml-native cli

You can now use the [enaml-native-cli](https://github.com/codelv/enaml-native-cli) instead of
installing from source. Simply use:

  
```bash

conda install -c codelv enaml-native-cli

```

### Create and run a new project

To create a new project use the cli to init a new project.

```bash

# Within the folder of choice
enaml-native create app

```

Now cd to the destination folder, activate the virtual env, and build the python and ndk libraries.

```bash
    
#: Go into project folder
cd HelloWorld

#: Activate the venv
source activate ./venv

```

Now either start the emulator or plug in a phone and we can run with
 
```bash
     
enaml-native run-android
 
```
 

Your app's code resides in the `src` directory. Any files here get installed on the app.

The `view.enaml` contains the UI that is shown, and `main.py` is the startup script. 

### Installing packages

To include 3rd-party python packages in your app they must first be built for Android or iOS, then installed into your apps virtual environment.  Enaml-native uses [conda](https://conda.io/docs/user-guide/getting-started.html) as it's package manager as it helps handle the complexity of cross compiling for Android and iOS (see [conda-mobile](https://github.com/codelv/conda-mobile) if your interested).  

The `enaml-native` command includes a wrapper for conda to install packages. `enaml-native-icons` is a package that lets you use font based icons in your app. To install it run:

```bash
enaml-native install enaml-native-icons
```

or use with conda directly

```bash
conda install -c codelv enaml-native-icons
```

Once installed you can rebuild the app and your new packages should be available on the app!  

If you run into issues, you can ask for help on [gitter](https://gitter.im/enaml-native/Lobby).

> When installing packages with conda you need to specify the `-c codelv` flag to tell conda to include packages from the [codelv](https://anaconda.org/codelv/repo) channel which contains packages precompiled for android and iOS. If you prefer, you can add it as a default channel by running `conda config --append channels codelv` (see https://conda.io/docs/user-guide/tasks/manage-channels.html).


Next [learn the basics](https://www.codelv.com/projects/enaml-native/docs/learn-the-basics)
