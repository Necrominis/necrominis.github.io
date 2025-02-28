# About This Repository

This is a Python-based program to generate the HTML files for my website (https://necrominis.github.io).

The main reason for this program is that it generates static HTML pages, rather than more dynamic websites like those made with React or Vue. This lets me host the site on GitHub Pages, without the need for a server, and it also gives me control over the HTML structure, the URL paths, etc. Finally, it also means pages can operate faster, as they don't need to make as many server requests and they don't use as much JavaScript.

The other reason for this program is that it enables me to decouple the page data from the page files themselves. All the actual page data is stored in a large Python dictionary (which I've learned isn't perfect and I might change later). This means that I can change the HTML page layouts or even the entire website's structure without affecting the core data on the pages.

This method also gives me easier data validation, as I can write Python code to check for issues. Plus Python gives me IntelliSense to validate my data (i.e. code) as I type it, which SQL databases don't have, meaning you have to create forms and such.

# Generating the Webpages

The current working directory must be the root folder of this repository (not the `.builder` folder) to work properly.

```bash
cd ~/dev/necrominis.github.io
python3 .builder/main.py
```

## Arguments

### Verbose

The following are identical syntaxes for the verbose argument.

```bash
python3 .builder/main.py -v
python3 .builder/main.py -verbose
python3 .builder/main.py --verbose
```

Prints out the website URL and the absolute filepath of every page's `index.html` during generation, in addition to the page's relative path.

### Silent

The following are identical syntaxes for the silent argument.

```bash
python3 .builder/main.py -s
python3 .builder/main.py -silent
python3 .builder/main.py --silent
```

Hides the printing of every page during generation, leaving only a starting and finished print-out.

### Clean

**_This argument is planned but not implemented yet!_**

The following are identical syntaxes for the clean argument.

```bash
python3 .builder/main.py -c
python3 .builder/main.py -clean
python3 .builder/main.py --clean
```

Deletes all nonessential files, before generating the new website files, in order to clear out any files that would no longer exist when rebuilding.

### Directory

**_This argument is planned but not implemented yet!_**

The following are identical syntaxes for the directory argument.

```bash
python3 /path/to/necrominis.github.io/.builder/main.py -d "/path/to/necrominis.github.io/"
python3 /path/to/necrominis.github.io/.builder/main.py -dir "/path/to/necrominis.github.io/"
python3 /path/to/necrominis.github.io/.builder/main.py --dir "/path/to/necrominis.github.io/"
python3 /path/to/necrominis.github.io/.builder/main.py -directory "/path/to/necrominis.github.io/"
python3 /path/to/necrominis.github.io/.builder/main.py --directory "/path/to/necrominis.github.io/"
```

Changes the current working directory within the script to the given path. The path must lead to this repository's root folder in order to work.

# To-Do

## Planned Features

* Add sorting to tags.
* Add sorting to manufacturers.
* Add previous/next post buttons.
* Add filter input to gallery URL.
	* Have tags link to their filtered gallery specifically.
* Add page footer.
* Implement the clean argument's functionality.
* Implement the directory argument's functionality.
* Add a related posts gallery below post articles (ideally with the same tags/filters as the post itself).
* Add paints page.
	* Have paints page get paints automatically, without having to list them specifically.
* Add supplies page.
	* Have supplies page get supplies automatically, without having to list them specifically.
* Add slideshow to modal.
* Add redirect links for posts based on title.

## Unimplemented Code

* `build_paints_article_content_html()`
* `build_paint_article_content_html()`
* `build_supplies_article_content_html()`
* `build_supply_article_content_html()`

## Open Issues

## Posts & Photos

* Post 2023-02-17 (Adeptus Mechanicus Skitarii Ranger) has no photos.

## Un-Added Data

* Add my camera.
* Add the backdrop papers.
* Add my plastic drawers.
* Add hobby knife.
	* Update paragraphs in post 2023-02-17.