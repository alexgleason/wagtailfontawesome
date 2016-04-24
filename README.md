Wagtail FontAwesome
====================
Add [FontAwesome](https://github.com/FortAwesome/Font-Awesome) icons to StreamField.

![Screenshot](screenshot.png)

Install
-------

    pip install wagtailfontawesome

Then add `wagtailfontawesome` to your installed apps.

Usage
-----
### StreamField
Add FontAwesome icons to StreamField [the regular way](http://docs.wagtail.io/en/latest/topics/streamfield.html#basic-block-types), just set `icon="fa-something"`. Reference [the full list](http://fontawesome.io/icons/).

### wagtailmodeladmin
[wagtailmodeladmin](https://github.com/rkhleics/wagtailmodeladmin) is supported if you're using Wagtail 1.4 or above. Similar to StreamField, just set `icon="fa-something"` on your menu item.

### Hallo plugins
You can use FontAwesome icons on custom Hallo buttons by setting the `icon` option to `icon icon-fa-something`.

    button.hallobutton({
      label: "Blockquote",
      icon: 'icon icon-fa-quote-left',
    });

### Other areas
You can include icons anywhere with `<i class="icon icon-fa-something"></i>`. In Wagtail 1.3.x and below you can only use icons on the page editor screen.
