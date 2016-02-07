Title: Install ffmpeg under Windows 10 with MSYS2 and MINGW64
Date: 2016-02-07 18:09
Category: ffmpeg
Tags: ffmpeg, msys2, mingw64, windows

### Assumptions

- You have PC with Windows 64 bit and internet access
- You want to target 32-bit platform

### Steps:

1. Install MSYS2 (x86_64) package from https://msys2.github.io/ into `C:\msys64`

2. Start `C:\msys64\msys2_shell.bat`

3. Run the following commands to provision MSYS2 environments with necessary tools:

        pacman -S make pkgconf diffutils
        update-core
        # restart MSYS2
        pacman -Su
        # restart MSYS2
        pacman -S mingw-w64-i686-yasm mingw-w64-i686-nasm mingw-w64-i686-gcc mingw-w64-i686-toolchain mingw-w64-i686-cmake mingw-w64-i686-extra-cmake-modules mingw-w64-i686-SDL
        pacman -S base-devel grep sed gzip tar wget perl autoconf automake libtool

4. Compile libfdk_aac:
   
        cd ~
        git clone https://github.com/mstorsjo/fdk-aac.git
        cd fdk-aac
        ./autogen.sh
        ./configure --prefix=/mingw --disable-shared --enable-static
        make
        make install

5. Compile libmp3lame

    Remove `xmmintrin.h \` line from file `configure`.

        cd ~    
        wget http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz
        tar xzvf lame-3.99.5.tar.gz
        cd lame-3.99.5
        ./configure --prefix="/mingw" --enable-nasm --disable-shared --build=mingw32
        make
        make install
        make distclean        
    
6. Compile libx264

        cd ~
        wget http://download.videolan.org/pub/x264/snapshots/last_x264.tar.bz2
        tar xjvf last_x264.tar.bz2
        cd x264-snapshot*
        ./configure --prefix=/mingw --host=i686-w64-mingw32 --enable-static
        make
        make install
        make distclean
        
7. Compile libx265

        cd ~
        hg clone https://bitbucket.org/multicoreware/x265
        cd ~/x265/build/linux
        cmake -G "MSYS Makefiles" -DCMAKE_INSTALL_PREFIX=/mingw -DENABLE_SHARED:bool=off ../../source
        make
        make install
        make distclean
        
8. Compile libopus

        cd ~
        wget http://downloads.xiph.org/releases/opus/opus-1.1.tar.gz
        tar xzvf opus-1.1.tar.gz
        cd opus-1.1
        ./configure --prefix="/mingw" --disable-shared --enable-static
        make
        make install
        make clean

8. Compile ffmpeg

        export PKG_CONFIG_PATH=/mingw/lib/pkg:$PKG_CONFIG_PATH
        ./configure --prefix=/mingw --enable-gpl --enable-nonfree --enable-libfdk-aac --enable-libmp3lame --enable-libx264 --enable-libx265 --enable-libopus --extra-cflags="-I/mingw/include" --extra-ldflags="-L/mingw/lib" --pkg-config-flags="--static"
