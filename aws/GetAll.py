#! /usr/bin/python
#
import sys
import os
import time
import boto.ec2.connection

f = open('setup/ak', 'r')
ak = f.readline()
f.close()
f = open('setup/sk', 'r')
sk = f.readline()
f.close()

ec2conn = boto.ec2.connection.EC2Connection(ak,sk)
reservations = ec2conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for i in instances:
    pprint(i.__dict__)
    break # remove this to list all instances
