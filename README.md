# Opal Observations

Observations plugin for Opal

Record patient observations (BP/Sp02/RR/ et cetera) and visualise trends over time in Opal.

[![Build Status](https://travis-ci.org/openhealthcare/opal-observations.svg?branch=v0.5.0)](https://travis-ci.org/openhealthcare/opal-observations)

## Installation

Add 'obs' to INSTALLED_APPLICATIONS in your implementation's `settings.py`.

Then, run:

    $ python manage.py migrate

Add observation to your schemas as required.
