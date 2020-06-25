# Notetaker

The Notetaker is an easy to use command line note taking application written in python. Flexiblity is added through a JSON based configuration file.

## Usage

```
py Notetaker.py --file FileName --header
```

## Configuration

Things to configure:

* Text Editor to work on notes
* Default author name
* Elements of notes header (Date/Time, Author, ...)

Example Configuration File:
```
{
  "textEditor":"code",
  "author":"John Doe",
  "noteHeader": {
    "dateTime":True,
    "Author":False
  }
}
```
