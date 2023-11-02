<<<<<<< HEAD
This is the first README file in this directory
=======
# README File
This is the readme file for this directory.

# About api directory
This directory contains all tasks.

# Task Number
Number: 0

# Task Name
Gather data from an API

# About
Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

Requirements:

* You must use `urllib` or `requests module`
* The script must accept an integer as a parameter, which is the employee ID
* The script must display on the standard output the employee TODO list progress in this exact format:
    * First line: Employee `EMPLOYEE_NAME` is done with tasks(`NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS`):
        * `EMPLOYEE_NAME`: name of the employee
        * `NUMBER_OF_DONE_TASKS`: number of completed tasks
        * `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
    * Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`)

Example:

`sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2`

`Employee Ervin Howell is done with tasks(8/20):`
     `distinctio vitae autem nihil ut molestias quo`
     `voluptas quo tenetur perspiciatis explicabo natus`
     `aliquam aut quasi`
     `veritatis pariatur delectus`
     `nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis`
     `repellendus veritatis molestias dicta incidunt`
     `excepturi deleniti adipisci voluptatem et neque optio illum ad`
     `totam atque quo nesciunt`

`sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4`

`Employee Patricia Lebsack is done with tasks(6/20):`
     `odit optio omnis qui sunt`
     `doloremque aut dolores quidem fuga qui nulla`
     `sint amet quia totam corporis qui exercitationem commodi`
     `sequi dolorem sed`
     `eum ipsa maxime ut`
     `tempore molestias dolores rerum sequi voluptates ipsum consequatur`

`sylvain@ubuntu$`

`sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T"`

`Employee Patricia Lebsack is done with tasks(6/20):`
`TSodit optio omnis qui sunt`
`TSdoloremque aut dolores quidem fuga qui nulla`
`TSsint amet quia totam corporis qui exercitationem commodi`
`TSsequi dolorem sed`
`TSeum ipsa maxime ut`
`TStempore molestias dolores rerum sequi voluptates ipsum consequatur`
`sylvain@ubuntu$`

### Repo
* GitHub repository: `alu-back-end`
* Directory: `api`
* File: `0-gather_data_from_an_API.py`
>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
