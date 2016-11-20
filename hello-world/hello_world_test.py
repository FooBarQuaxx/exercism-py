# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import hello_world
import pytest


def test_hello_without_name():
    assert 'Hello, World!' == hello_world.hello()


def test_hello_with_sample_name():
    assert 'Hello, Alice!' == hello_world.hello('Alice')


def test_hello_with_other_sample_name():
    assert 'Hello, Bob!' == hello_world.hello('Bob')


def test_hello_with_umlaut_name():
    assert 'Hello, Jürgen!' == hello_world.hello('Jürgen')


def test_hello_with_blank_name():
    assert 'Hello, World!' == hello_world.hello('')


def test_hello_with_none_name():
    assert 'Hello, World!' == hello_world.hello(None)

if __name__ == '__main__':
    pytest.main()
