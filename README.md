# GL_DevOps_ProCamp


### Install

Build from Dockerfile:

    docker build -t test_task -f Dockerfile .

### Run

Run the image:

    docker run --pid=host -v /proc/:/app/proc:ro -it test_task /bin/bash
    
### Use monitor script

Inside the docker container run following command to get CPU or MEM usage:

    python server_monitor.py cpu
    python server_monitor.py mem

    

