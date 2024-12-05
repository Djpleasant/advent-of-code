# djpleasant - AoC

This is a collection of my [Advent of Code](https://adventofcode.com/)
attempts across the years.

In each year directory, there will be a README.md file. This file will detail
what my goals were for this year's AoC. I want to try and use this event as a
way to learn different tools or languages.

So if you are interested in what I was trying to do on a particular year, take
a look at that file.

One other larger goal is to compile a timeline of my development habits and
various techniques I may pick up during a specific year. I want to do this
because pointing and laughing at past-me is my favorite activity,
but it may also be useful for others to see my work since I intend to keep
things readable.

Will it be testable? I'd be a fool to commit that to the proverbial stone but
I'll try my best.

# Pre-requisites

- [uv](https://github.com/astral-sh/uv)

This is the tool that manages the python environments. I would describe it
as "quite good".

- [Python](https://www.python.org/)

`uv` may be able to install Python if it is missing on your system, but I'm
sure there's still libraries that will be needed.
So you'll probably chicken and egg yourself if you don't have a python
interpreter on your system already.

- [shell](https://www.gnu.org/software/bash/)

The shell scripts in this project SHOULD be POSIX-compatible, so most any
shell flavour will work. I MAY add in Windows scripts in the future, but no
promises there, partner.

# Basic Usage

As of this writing, you will want to refer to a specific year's structure to
determine how to re-run past solutions. With the way I'm setting it up, I
think it should be trivial to implement, but the AGILE training I've recently
been forced to watch has told me that I don't HAVE to do this right now.

# Documentation

To build the documentation site, please ensure your system meets the
[pre-requisites](#pre-requisites) listed earlier in this document.


Steps:

1.) Install the python project.

```sh
scripts/install
```

2.) Build the documentation site.

```sh
scripts/docs
```

3.) Serve the documentation site locally.

```sh
scripts/docs_serve
```
