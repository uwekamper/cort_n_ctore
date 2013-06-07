cort_n_ctore
============

Sort and Store. This is a very small database with a small webinterface and a REST-API, built with django. It is used to keep track of the enormous amounts of electronical parts, that the c-lab aquired. We want to give Users the ability to search through a database of boxes for the part they require, instead of manually searching through countless boxes.








API
===

GET /places/

  List of places

GET /types/

  List of General Types

GET /types/<GENERAL>

  List of Specific Types in the given General Type

GET /parts/?[general=*][specific=*][value=*][place=*][package=*]

  List of Parts that match the filter
