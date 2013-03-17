## About

**flickerget** is a simple Python script that finds the download link for ever image in any user's Flickr set. Every download link is the largest version of the image.

It is inspired by the UNIX philosophy of doing one thing only and doing it well.

## Usage

Invoking the script is simple:

	flickrget.py -i URL -o OUTPUT

At the very least you must supply an input URL. For example:

	flickrget.py -i http://www.flickr.com/photos/benroffelsen/sets/72157631898699655/

This will display all output to stdout.

Keep in mind that so far **flickrget** only works with user sets, and not photostreams or any other type of top-level link.

To pipe all output into a file, use `-o`:

	flickrget.py -i http://www.flickr.com/photos/benroffelsen/sets/72157631898699655/ -o /home/user/flickr_links

To download the images, you can pipe output into `wget`. Once you have all image links in a file:

    wget -i /home/user/flickr_links

Or, you can pipe output directly:

	flickrget.py -i http://www.flickr.com/photos/benroffelsen/sets/72157631898699655/ | wget -i -

I recommend putting the script somewhere on your `$PATH` or aliasing it together with wget for ease of use.

## Why

Someone somewhere posted a link to an image on Flickr that I thought would have 
made a fantastic wallpaper. However, when I saw that "downloads" were disabled, 
I had to manually retrieve that image. This wasn't so bad except that *all* the
images in that particular set were so good they could have been wallpapers. So,
I hacked up this small script to do it for me.

The script can also be used for archival purposes, and as an emergency backup
if for some reason your images stop existing everywhere but Flickr.

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any
later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.
