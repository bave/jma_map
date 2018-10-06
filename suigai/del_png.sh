#!/bin/sh

ls | grep "\.png" | xargs -I xxx rm xxx
