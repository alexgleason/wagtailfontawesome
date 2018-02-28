===================
Wagtail FontAwesome
===================
.. image:: https://travis-ci.org/alexgleason/wagtailfontawesome.svg?branch=master
    :target: https://travis-ci.org/alexgleason/wagtailfontawesome
.. image:: https://coveralls.io/repos/github/alexgleason/wagtailfontawesome/badge.svg?branch=master
    :target: https://coveralls.io/github/alexgleason/wagtailfontawesome?branch=master
.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
    :target: https://github.com/alexgleason/wagtailfontawesome/blob/master/LICENSE

Add `FontAwesome 4.7 <https://fontawesome.com/v4.7.0/>`_ icons to StreamField.

.. image:: https://raw.githubusercontent.com/alexgleason/wagtailfontawesome/master/screenshot.png
    :alt: Screenshot

Install
=======

.. code-block:: console

    pip install wagtailfontawesome


Then add ``wagtailfontawesome`` to your installed apps.

Usage
=====

StreamField
-----------

Add FontAwesome icons to StreamField `the regular way <http://docs.wagtail.io/en/latest/topics/streamfield.html#basic-block-types>`_, just set `icon="fa-something"`. Reference `the full list <http://fontawesome.io/icons/>`_.

wagtailmodeladmin
-----------------

`wagtailmodeladmin <https://github.com/rkhleics/wagtailmodeladmin>`_ is supported if you're using Wagtail 1.4 or above. Similar to StreamField, just set `icon="fa-something"` on your menu item.

Hallo plugins
-------------

You can use FontAwesome icons on custom Hallo buttons by setting the `icon` option to `icon icon-fa-something`.

.. code-block:: javascript

    button.hallobutton({
      label: "Blockquote",
      icon: 'icon icon-fa-quote-left',
    });

Other parts of the admin
------------------------

You can include icons anywhere in the admin with:

.. code-block:: html+django

    <i class="icon icon-fa-something"></i>

In Wagtail 1.3.x and below you can only use icons on the page editor screen.

On the front-end
----------------

You can also include the CSS on the front end, and follow FontAwesome's documentation.

.. code-block:: html+django

    {% load wagtailfontawesome %}

    {% fontawesome_css %}

This will generate equivalent markup to:

.. code-block:: html+django

    <link rel="stylesheet" href="{% static 'wagtailfontawesome/css/fontawesome.css' %}">

Then include icons anywhere on the front-end with:

.. code-block:: html+django

    <i class="fa fa-something"></i>

Using wagtailfontawesome as an optional dependency
--------------------------------------------------

If you want to distribute a Wagtail plugin with FontAwesome icons, you can use this package as an optional dependency by checking if it's installed in Django, and falling back otherwise.

.. code-block:: python

    from django.apps import apps
    try:
        from wagtail.core.blocks import StructBlock
    except ImportError:  # fallback for Wagtail <2.0
        from wagtail.wagtailcore.blocks import StructBlock


    class BlockquoteBlock(StructBlock):
        quote = TextBlock()
        author = TextBlock()

        class Meta:
            if apps.is_installed('wagtailfontawesome'):
                icon = 'fa-quote-left'

(in this case, the fallback is to do nothing)
