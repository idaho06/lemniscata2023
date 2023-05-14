# Rediscovering A Vintage Masterpiece

It's perfectly reasonable to refer to 25-year-old code as "retro-code." I like to apply this term to code that was written in earlier stages of computer programming, which now serves as a testament to the history and evolution of the field. Similar to "retro" items in other fields, like fashion or gaming, "retro-code" represents older styles or techniques that are still of interest in the present day, whether for historical, educational, or nostalgic reasons.

![Book](https://u.cubeupload.com/idaho06/Screenshotfrom202305.png)

Lately, I've been diving into the classic text ["OpenGL Programming for the X Window System" by Mark J. Kilgard](https://amzn.eu/d/c0YMsXa). This book, dating back to 1996, is a fascinating look at the early days of creating applications with OpenGL for graphics and the X Window System.

While the technology landscape has significantly evolved since then, what captured my interest is the longevity of the code. Yes, the code examples from this 1996 book still compile and run perfectly on modern Linux distributions!

## Resurrecting Code from the Past
I stumbled upon an [old FTP mirror](https://ftp.zx.net.nz/pub/mirror/ftp.sgi.com/opengl/OLD/opengl_for_x/) hosting the source code for the book. With a few attempts, to my surprise, I managed to get it up and running.

<pre>
idaho@pop-os:~$ cd Projects/
idaho@pop-os:~/Projects$ wget https://ftp.zx.net.nz/pub/mirror/ftp.sgi.com/opengl/OLD/opengl_for_x/glut.tar.Z
--2023-05-14 13:28:41--  https://ftp.zx.net.nz/pub/mirror/ftp.sgi.com/opengl/OLD/opengl_for_x/glut.tar.Z
Resolving ftp.zx.net.nz (ftp.zx.net.nz)... 123.255.63.188
Connecting to ftp.zx.net.nz (ftp.zx.net.nz)|123.255.63.188|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 671785 (656K) [application/x-compress]
Saving to: ‘glut.tar.Z’

glut.tar.Z          100%[===================>] 656,04K   419KB/s    in 1,6s    

2023-05-14 13:28:44 (419 KB/s) - ‘glut.tar.Z’ saved [671785/671785]

idaho@pop-os:~/Projects$ tar -xzvf glut.tar.Z 
opengl_for_x/
[...]
idaho@pop-os:~/Projects$ cd opengl_for_x/
idaho@pop-os:~/Projects/opengl_for_x$ ll
total 12
drwxr-xr-x  3 idaho idaho 4096 nov 21  1996 ./
drwxrwxr-x 16 idaho idaho 4096 may 14 13:29 ../
drwxr-xr-x 15 idaho idaho 4096 nov 21  1996 glut/
idaho@pop-os:~/Projects/opengl_for_x$ cd glut/
idaho@pop-os:~/Projects/opengl_for_x/glut$ ll
total 68
drwxr-xr-x 15 idaho idaho 4096 nov 21  1996 ./
drwxr-xr-x  3 idaho idaho 4096 nov 21  1996 ../
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 blender/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 doc/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 GL/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 glutduck/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 glutsphere/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 libglut/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 lightlab/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 mjkwarp/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 molehill/
-rw-r--r--  1 idaho idaho  544 ago 23  1996 NOTICE
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 origami/
-rw-r--r--  1 idaho idaho 1271 ago 23  1996 README
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 splatlogo/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 torus_test/
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 zoomdino/
idaho@pop-os:~/Projects/opengl_for_x/glut$
 
</pre>

Let's try to compile `glutsphere`, one of the first examples in the book.

<pre>
idaho@pop-os:~/Projects/opengl_for_x/glut$ cd glutsphere/
idaho@pop-os:~/Projects/opengl_for_x/glut/glutsphere$ ll
total 16
drwxr-xr-x  2 idaho idaho 4096 nov 21  1996 ./
drwxr-xr-x 15 idaho idaho 4096 nov 21  1996 ../
-rw-r--r--  1 idaho idaho 1541 ago 23  1996 glutsphere.c
-rw-r--r--  1 idaho idaho  261 nov 21  1996 Makefile
idaho@pop-os:~/Projects/opengl_for_x/glut/glutsphere$ make
cc -I.. -O   -c -o glutsphere.o glutsphere.c
cd ../libglut ; make libglut.a
make[1]: Entering directory '/home/idaho/Projects/opengl_for_x/glut/libglut'
cc -I.. -O   -c -o glut_bitmap.o glut_bitmap.c
cc -I.. -O   -c -o glut_bwidth.o glut_bwidth.c
cc -I.. -O   -c -o glut_cindex.o glut_cindex.c
cc -I.. -O   -c -o glut_cursor.o glut_cursor.c
cc -I.. -O   -c -o glut_dials.o glut_dials.c
cc -I.. -O   -c -o glut_event.o glut_event.c
cc -I.. -O   -c -o glut_ext.o glut_ext.c
cc -I.. -O   -c -o glut_fullscrn.o glut_fullscrn.c
cc -I.. -O   -c -o glut_get.o glut_get.c
cc -I.. -O   -c -o glut_init.o glut_init.c
cc -I.. -O   -c -o glut_input.o glut_input.c
glut_input.c: In function ‘probeDevices’:
glut_input.c:276:27: warning: cast from pointer to integer of different size [-Wpointer-to-int-cast]
  276 |   if (version == NULL || ((int) version) == NoSuchExtension) {
      |                           ^
glut_input.c: At top level:
glut_input.c:506:1: warning: return type defaults to ‘int’ [-Wimplicit-int]
  506 | glutDeviceGet(GLenum param)
      | ^~~~~~~~~~~~~
cc -I.. -O   -c -o glut_menu.o glut_menu.c
cc -I.. -O   -c -o glut_modifier.o glut_modifier.c
cc -I.. -O   -c -o glut_overlay.o glut_overlay.c
glut_overlay.c:18:10: fatal error: X11/Xmu/StdCmap.h: No such file or directory
   18 | #include <X11/Xmu/StdCmap.h>  /* for XmuLookupStandardColormap */
      |          ^~~~~~~~~~~~~~~~~~~
compilation terminated.
make[1]: *** [<builtin>: glut_overlay.o] Error 1
make[1]: Leaving directory '/home/idaho/Projects/opengl_for_x/glut/libglut'
make: *** [Makefile:10: ../libglut/libglut.a] Error 2
idaho@pop-os:~/Projects/opengl_for_x/glut/glutsphere$ 
</pre>

It looks like a library header is missing.

<pre>
idaho@pop-os:~/Projects/opengl_for_x/glut/glutsphere$ sudo apt install libxmu-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libxmu-headers
The following NEW packages will be installed:
  libxmu-dev libxmu-headers
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 109 kB of archives.
After this operation, 535 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://apt.pop-os.org/ubuntu jammy/main amd64 libxmu-headers all 2:1.1.3-3 [54,1 kB]
Get:2 http://apt.pop-os.org/ubuntu jammy/main amd64 libxmu-dev amd64 2:1.1.3-3 [54,6 kB]
Fetched 109 kB in 0s (665 kB/s)      
Selecting previously unselected package libxmu-headers.
(Reading database ... 347127 files and directories currently installed.)
Preparing to unpack .../libxmu-headers_2%3a1.1.3-3_all.deb ...
Unpacking libxmu-headers (2:1.1.3-3) ...
Selecting previously unselected package libxmu-dev:amd64.
Preparing to unpack .../libxmu-dev_2%3a1.1.3-3_amd64.deb ...
Unpacking libxmu-dev:amd64 (2:1.1.3-3) ...
Setting up libxmu-headers (2:1.1.3-3) ...
Setting up libxmu-dev:amd64 (2:1.1.3-3) ...
idaho@pop-os:~/Projects/opengl_for_x/glut/glutsphere$
</pre>

Let's try again.

<pre>
idaho@pop-os:~/Projects/opengl_for_x/glut/glutsphere$ make
cd ../libglut ; make libglut.a
make[1]: Entering directory '/home/idaho/Projects/opengl_for_x/glut/libglut'
cc -I.. -O   -c -o glut_overlay.o glut_overlay.c
cc -I.. -O   -c -o glut_shapes.o glut_shapes.c
cc -I.. -O   -c -o glut_space.o glut_space.c
cc -I.. -O   -c -o glut_stroke.o glut_stroke.c
cc -I.. -O   -c -o glut_swidth.o glut_swidth.c
cc -I.. -O   -c -o glut_tablet.o glut_tablet.c
cc -I.. -O   -c -o glut_teapot.o glut_teapot.c
cc -I.. -O   -c -o glut_util.o glut_util.c
cc -I.. -O   -c -o glut_win.o glut_win.c
cc -I.. -O   -c -o glut_winmisc.o glut_winmisc.c
cc -I.. -O   -c -o glut_8x13.o glut_8x13.c
cc -I.. -O   -c -o glut_9x15.o glut_9x15.c
cc -I.. -O   -c -o glut_hel10.o glut_hel10.c
cc -I.. -O   -c -o glut_hel12.o glut_hel12.c
cc -I.. -O   -c -o glut_hel18.o glut_hel18.c
cc -I.. -O   -c -o glut_tr10.o glut_tr10.c
cc -I.. -O   -c -o glut_tr24.o glut_tr24.c
cc -I.. -O   -c -o glut_roman.o glut_roman.c
cc -I.. -O   -c -o glut_mroman.o glut_mroman.c
cc -I.. -O   -c -o layerutil.o layerutil.c
ar cr libglut.a glut_bitmap.o glut_bwidth.o glut_cindex.o glut_cursor.o glut_dials.o glut_event.o glut_ext.o glut_fullscrn.o glut_get.o glut_init.o glut_input.o glut_menu.o glut_modifier.o glut_overlay.o glut_shapes.o glut_space.o glut_stroke.o glut_swidth.o glut_tablet.o glut_teapot.o glut_util.o glut_win.o glut_winmisc.o glut_8x13.o glut_9x15.o glut_hel10.o glut_hel12.o glut_hel18.o glut_tr10.o glut_tr24.o glut_roman.o glut_mroman.o layerutil.o
make[1]: Leaving directory '/home/idaho/Projects/opengl_for_x/glut/libglut'
cc -o glutsphere glutsphere.o -L../libglut -lglut -lGL -lGLU -lXmu -lXext -lX11 -lm
idaho@pop-os:~/Projects/opengl_for_x/glut/glutsphere$
</pre>

There you go! No warnings, clean compilation.

![First try!](https://u.cubeupload.com/idaho06/8feScreenshotfrom202305.png)

Another example. This does not compile so cleanly.

<pre>
idaho@pop-os:~/Projects/opengl_for_x/glut$ cd zoomdino/
idaho@pop-os:~/Projects/opengl_for_x/glut/zoomdino$ ll
total 24
drwxr-xr-x  2 idaho idaho  4096 nov 21  1996 ./
drwxr-xr-x 15 idaho idaho  4096 nov 21  1996 ../
-rw-r--r--  1 idaho idaho   249 nov 21  1996 Makefile
-rw-r--r--  1 idaho idaho 11345 ago 23  1996 zoomdino.c
idaho@pop-os:~/Projects/opengl_for_x/glut/zoomdino$ make
cc -I.. -O   -c -o zoomdino.o zoomdino.c
zoomdino.c: In function ‘extrudeSolidFromPolygon’:
zoomdino.c:60:38: warning: passing argument 3 of ‘gluTessCallback’ from incompatible pointer type [-Wincompatible-pointer-types]
   60 |     gluTessCallback(tobj, GLU_BEGIN, glBegin);
      |                                      ^~~~~~~
      |                                      |
      |                                      void (*)(GLenum) {aka void (*)(unsigned int)}
In file included from ../GL/glut.h:11,
                 from zoomdino.c:14:
/usr/include/GL/glu.h:336:87: note: expected ‘_GLUfuncptr’ {aka ‘void (*)(void)’} but argument is of type ‘void (*)(GLenum)’ {aka ‘void (*)(unsigned int)’}
  336 | essCallback (GLUtesselator* tess, GLenum which, _GLUfuncptr CallBackFunc);
      |                                                 ~~~~~~~~~~~~^~~~~~~~~~~~

zoomdino.c:61:39: warning: passing argument 3 of ‘gluTessCallback’ from incompatible pointer type [-Wincompatible-pointer-types]
   61 |     gluTessCallback(tobj, GLU_VERTEX, glVertex2fv);  /* semi-tricky
      |                                       ^~~~~~~~~~~
      |                                       |
      |                                       void (*)(const GLfloat *) {aka void (*)(const float *)}
In file included from ../GL/glut.h:11,
                 from zoomdino.c:14:
/usr/include/GL/glu.h:336:87: note: expected ‘_GLUfuncptr’ {aka ‘void (*)(void)’} but argument is of type ‘void (*)(const GLfloat *)’ {aka ‘void (*)(const float *)’}
  336 | essCallback (GLUtesselator* tess, GLenum which, _GLUfuncptr CallBackFunc);
      |                                                 ~~~~~~~~~~~~^~~~~~~~~~~~

cc -o zoomdino zoomdino.o -L../libglut -lglut -lGL -lGLU -lXmu -lXext -lX11 -lm
idaho@pop-os:~/Projects/opengl_for_x/glut/zoomdino$ 
</pre>

But still...

![Dino](https://u.cubeupload.com/idaho06/b06Screenshotfrom202305.png)

And one more.

![blender](https://u.cubeupload.com/idaho06/Screencastfrom140523.gif)

This has been a delightful journey, a sort of software archaeology, delving into the past and unearthing treasures that still hold their value today.

It's a testament to the robustness and forward-compatibility of both OpenGL and the X Window System that these examples can still be compiled and executed. The code is over two decades old, yet it stands the test of time.

## What We Can Learn
This is a perfect reminder that while technology continues to progress at a breakneck pace, the foundations remain remarkably consistent. The principles and techniques we learn today can have relevance and value far into the future, just as the teachings from this classic text still do.

Whether you're a seasoned developer or just starting your journey, there's value in revisiting these classics. Not only do they provide a solid understanding of the basics, but they also offer a window into how far we've come, and yet how some things remain the same.