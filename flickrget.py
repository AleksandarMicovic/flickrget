#!/usr/bin/python

# Author: Aleksandar Micovic <me@aleks.rs>
# Date: March 2013
#
# Questions? Comments? Let me know!
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or any
# later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.


from BeautifulSoup import BeautifulSoup as bs
from urllib2 import urlopen
import getopt
import sys

SUFFIXES = ['o', 'k', 'h', 'l', 'c', 'z', 'm', 'n', 's', 'q', 'sq', 't']

def get_picture_link(user_id, photo_id):
    photo_link = None
    
    for suffix in SUFFIXES:
        url = 'http://www.flickr.com/photos/' + user_id + '/' + photo_id + '/sizes/' + suffix + '/'
        response = urlopen(url)

        if response.url.split('/')[-2] != suffix:
            continue

        # Finally, the highest quality picture.
        soup = bs(response.read())
        photo_link = soup.find(id='allsizes-photo').find('img')['src']
        break

    return photo_link

def main(url, output):
    page = urlopen(url).read()
    user_id = url.split('http://www.flickr.com/photos/')[1].split('/')[0]
    soup = bs(page)
    pages_tag = soup.find(id='paginator-module')
    links = []

    if (pages_tag):
        pages = int(pages_tag['data-page-count'])
    else:
        pages = 1

    current_page = 1
    on_valid_page = True

    while on_valid_page:
        soup = bs(page)
        thumbnails = soup.findAll('div', 'photo-display-item')
        photo_ids = [div['data-photo-id'] for div in thumbnails]

        for photo_id in photo_ids:
            link = get_picture_link(user_id, photo_id)

            if output:
                links.append(link)
            else:
                print get_picture_link(user_id, photo_id)

        current_page += 1
        
        if current_page > pages:
            on_valid_page = False        
        else:
            page = urlopen(url + '?page=' + str(current_page)).read()

    if output:
        file_handler = open(output, 'w')
        file_handler.write('\n'.join(links))
        file_handler.close()


if __name__ == '__main__':
    HELP_STRING = "flickrget.py -i URL [-o OUTPUT_DIR]"
    url = ''
    output = None
    help_me = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:o:', ['help', 'url=', 'out='])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help_me = True
        elif opt in ("-i", "--url"):
            url = arg
        elif opt in ("-o", "--out"):
            output = arg
        elif opt in ('-v', '--verbose'):
            verbose = True

    if not opts or help_me or not url:
        print HELP_STRING
        sys.exit()
    else:
        main(url, output)
