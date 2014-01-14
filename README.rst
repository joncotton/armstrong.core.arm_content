armstrong.core.arm_content
==========================
Provides the foundation for all content inside Armstrong.

Usage
-----
You can use ``armstrong.core.arm_content`` to build out the custom models of
your site while following the DRY (Don't Repeat Yourself) principle.  It is the
foundation that the rest of the Armstrong content types are built off of.

For more information, please see the `full documentation`_.

.. change this link to point to docs inside docs.armstrongcms.org once its done
.. _full documentation: http://armstrong.github.io/armstrong.core.arm_content/


Installation & Configuration
----------------------------
#. ``pip install armstrong.core.arm_content``

#. Add ``taggit`` to your ``INSTALLED_APPS``

*Note:* You do not need to run ``syncdb`` or ``migrate`` after installing
because this component does not have any concrete models. For the same reason,
you do not need to add this to INSTALLED_APPS.

Optional Settings & Requirements:
"""""""""""""""""""""""""""""""""

To use the Sorl features, like ``SorlThumbnailMixin``, you'll need two things:
  #. Add ``sorl.thumbnail`` to your ``INSTALLED_APPS``

  #. Install an imaging library. Sorl supports several and you'll need one
     mentioned in their `docs`_.

To use the included template tags:
  #. Add ``armstrong.core.arm_content`` to your ``INSTALLED_APPS``

  #. Follow the above directions to install Sorl.


.. _docs: http://sorl-thumbnail.readthedocs.org/en/latest/requirements.html#image-library


State of Project
----------------
Armstrong is an open-source news platform that is freely available to any
organization. It is the result of a collaboration between the `Texas Tribune`_
and `The Center for Investigative Reporting`_ and a grant from the
`John S. and James L. Knight Foundation`_.

To follow development, be sure to join the `Google Group`_.

``armstrong.core.arm_content`` is part of the `Armstrong`_ project. You're
probably looking for that.


.. _Armstrong: http://www.armstrongcms.org/
.. _The Center for Investigative Reporting: http://cironline.org/
.. _John S. and James L. Knight Foundation: http://www.knightfoundation.org/
.. _Texas Tribune: http://www.texastribune.org/
.. _Google Group: http://groups.google.com/group/armstrongcms


License
-------
Copyright 2011-2014 Texas Tribune and The Center for Investigative Reporting

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
