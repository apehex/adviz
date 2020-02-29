# -*- coding: utf-8 -*-

"""
==============
Data Wrangling
==============

Clean the raw data scraped from the web.
"""

from __future__ import absolute_import, division, print_function

from bs4 import BeautifulSoup
from datetime import datetime
from nltk.metrics.distance import edit_distance
import numpy as np
import re

from typical import checks, iterable, numeric

#####################################################################
# CONSTANTS
#####################################################################

ANY_AREA_REGEX = '(\d+)\s*(?:m²|m2)?'
PRICE_REGEX = '([-+]?[0-9]*\.?[0-9]+)'

#####################################################################
# ENCODING & FORMAT
#####################################################################

@checks
def format_datetime(
        string: str,
        format: str) -> str:
    """
    Mold any serialized datetime to the ISO-8601 format.

    Example:
        27/02/2020 8:42
        => 2020-02-27T08:42:00 

    Parameters
    ----------
    string: str.
        A serialized datetime.
    format: str.
        Location of the relevant datetime values in the input string.

    Returns
    -------
    out: str.
        The serialized datetime with ISO-8601 format '%Y-%m-%dT%H:%M:%S'. 
    """
    return datetime.strptime(
        string,
        format).isoformat(sep='T', timespec='seconds')

@checks
def format_text(
        text: str) -> str:
    """
    Remove duplicate spacing and convert to lower case.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        The formated text.
    """
    return remove_extra_spacing(text.lower())

@checks
def format_number(
        text: str) -> numeric:
    """
    Convert strings to numpy float.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: np.float64.
        The formated text.
    """
    __as_text = format_text(text)
    __is_a_number = re.search(
        '([-+]?[0-9]+\.?[0-9]*).*',
        format_text(text))
    if __is_a_number:
        return np.float64(__is_a_number.group(1))
    else:
        return np.float64(np.nan)

#####################################################################
# TRANSLATION
#####################################################################

@checks
def string_distance(
        s1: str,
        s2: str) -> numeric:
    """
    Calculate a custom distance between strings.

    Does not take into account the difference in length.

    Parameters
    ----------
    s1: str.
        Any chunk of text.
    s2: str.
        Any chunk of text.

    Returns
    -------
    out: float.
        The distance between s1 and s2.
    """
    return (
        edit_distance(s1, s2)
        - abs(len(s1) - len(s2)))

@checks
def find_closest_reference(
        target: str,
        candidates: iterable,
        distance: callable=string_distance) -> str:
    """
    Find the element in an iterable closest to a given value.

    Parameters
    ----------
    target: str.
        The value to match.
    candidates: iterable.
        An iterable object in which the function picks.

    Returns
    -------
    out: str.
        The closest element from the target.
    """
    __distances = [
        distance(
            s1=target,
            s2=__s)
        for __s in candidates]
    return candidates[np.argmin(__distances)]

#####################################################################
# TEXT
#####################################################################

@checks
def remove_all_spacing(
        text: str) -> str:
    """
    Remove all the spaces in a string.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        The string without spaces.
    """
    return ''.join(text.split())

@checks
def remove_extra_spacing(
        text: str) -> str:
    """
    Replace any spacing by a single whitspace.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        A lean version of the input.
    """
    return ' '.join(text.split())

@checks
def remove_special_characters(
        text: str) -> str:
    """
    Replace all the special characters by '_'.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        A safe version of the input. 
    """
    return re.sub(
        '\W+',
        '_',
        text)

#####################################################################
# HTML
#####################################################################

@checks
def extract_text_from_html_markup(
        html: str) -> str:
    """
    Extract the text *visible* to a user on an internet browser,
    from a string of html markup.
    The chunks of text are separated by newlines.

    Parameters
    ----------
    html: str.
        A string of html markup soup.
    Returns
    -------
    out: str.
        The visible text.
    """
    __soup = BeautifulSoup(markup=html, features="lxml")

    # kill all script and style elements
    for script in __soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    __text = __soup.get_text(separator='.')

    # break into lines and remove leading and trailing space on each
    __lines = (
        __line.strip()
        for __line in __text.splitlines())
    # break multi-headlines into a line each
    __chunks = (
        __phrase.strip()
        for __line in __lines
        for __phrase in __line.split("."))
    # drop blank lines
    return '\n'.join(
        __chunk
        for __chunk in __chunks if __chunk)

@checks
def prettify_html(
        html: str) -> str:
    """
    Expand the html markup formatting:
    - break lines on opening tags
    - indent lines

    Parameters
    ----------
    html: str.
        A string of html markup soup.
    Returns
    -------
    out: str.
        The beautified html.
    """
    return BeautifulSoup(
        markup=html,
        features="lxml").prettify()

@checks
def serialize_html_tag(
        tag: str,
        value: str):
    """
    Serialize any tag as a string.

    Parameters
    ----------
    tag: str.
        The HTML tag type.
    value: str.
        The text enclosed in the tag.

    Returns
    -------
    out: str.
        The serialized HTML tag.
    """
    return '{}{}{}'.format(
        tag,
        value,
        tag.replace('<', '</'))

#####################################################################
# DATA MINING
#####################################################################

@checks
def extract_area_value(
        text: str) -> int:
    """
    Extract the numeric value of an area in a string like '102 m²'.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: int.
        A positive value of there's a match, -1 otherwise.
    """
    area_matches = re.search(ANY_AREA_REGEX, text, re.IGNORECASE)

    if area_matches:
        return int(area_matches.group(0))
    else:
        return -1

@checks
def extract_price_value(
        text: str) -> int:
    """
    Extract the numeric value of a price in a string like '320 €'.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: int.
        A positive value of there's a match, -1 otherwise.
    """
    area_matches = re.search(PRICE_REGEX, text, re.IGNORECASE)

    if area_matches:
        return int(float(area_matches.group(0)))
    else:
        return -1