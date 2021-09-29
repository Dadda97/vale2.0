# Vale2.0
Project created as Christmas present during the Covid-19 lockdown to reunite a family divided between two states.

To goal was to create a small version of Valentina, who was stuck in a foreign country, so that she could move around her house and virtually participate in the opening of presents on Christmas morning.

## Hardware

For starting, an old toy with electric drive wheels has been recovered and analyzed to understand how to make it move with some simple switches. From now on, this unit will be called "Asino": the Italian translation of "donkey" to express the limited feature it will provide, but also very similar to Asimo, a most famous humanoid robot.

To command the movement of Asino a USB computer control switch relay module was needed, for our architecture 8 relays were enough, so I bought one from [Amazon](https://www.amazon.it/gp/product/B07L12DXWB).

A battery and an old netbook have been fixed on Asino, in order to provide electricity to the motors and an easy way to command the relays module.

The following is a quick description of which relays are needed to perform an action; of course, this schema can be rearranged if necessary: 

    go forward : 8,3,
    go backward : 8,2,3,4,
    turn left : 3,2,8,
    turn right : 8,4,2,


## Software

### Asino
For managing the USB relay module installed on Asino I used [usbrelay](https://github.com/darrylb123/usbrelay) from darryb123, this allows me to open and close the switches from Python.

### Vale
A python script was used by Valentina to send the input to Asino. 

### Server 
To avoid problems with firewalls and static IPs a very simple server was implemented and hosted on a EC2 instance of AWS. It simply resend the input from Valentina to Asino. 
|||
:-------------------------:|:-------------------------:
<img src="img\init_asino.jpeg" width="800px">Initial structure of Asino| <img src="img\naked_asino.jpeg" width="800px">The "skeleton" of Asino|
<img src="img\pimped_asino.jpeg" width="800px">"Pimp" my Asino|<img src="img\asino_at_home.jpeg" width="800px">Asino at home

<p align="center">
    <img src="img\demo.gif"> Demo during develpment phase
</p>