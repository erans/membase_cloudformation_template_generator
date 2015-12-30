
=======================================================================================================
Membase is long dead (merged with CouchDB) and no body uses it anymore, least of all on CloudFormation. This is left here for case studies only and for tech archeology.
=======================================================================================================




UPDATE: Read more on this blog post: http://forecastcloudy.net/2011/12/06/membase-cluster-instead-of-elasticache-in-5-minutes/

Membase CloudFormation Template Generator
=========================================

Use this to generate CloudFormation (http://aws.amazon.com/cloudformation/) scripts to create Membase Server (http://www.couchbase.org/get/couchbase/current) Clusters in a few clicks. You can also use the template to add more servers to an existing cluster.
Use one of the pre-configured existing scripts (membase-pack-X) or use gen-pack.py to generate a new template with the number of servers you need.

This script is based on the CouchbaseLabs CloudFormation script located at: https://github.com/couchbaselabs/cloud-formation
I've updated it to support all instance types (including micro) and utilize the max amount of RAM per instance (80% of available RAM).

Script implementation comments:
===============================
* t1.micro instances use 32 bit to better utilize the 613MB available to it.
* All 32bit instances (t1.micro and m1.small) use EBS since it was easier to implement the generic script this way. This may change in the future.
* 64bit instances use instance store to maximize performance. You will have to add additional servers and/or update a backup script (read here about Membase backup and restore - http://www.couchbase.org/wiki/display/membase/Backup+and+Restore+with+Membase). This may also change in the future as I may introduce built-in backup to S3
* There are no monitoring scripts or way other than the built-in Membase console at the moment. This may change in the future with an added CloudWatch script support.


Benefits of using this template over AWS ElastiCache:
=====================================================
* Can be created on any region 
* Utilize Reserved Instance to significantly lower the cost (around 40%-60% reduction - check out the new reserved instances pricing: http://aws.typepad.com/aws/2011/12/reserved-instance-options-for-amazon-ec2.html - the heavy utilization seems like a perfect fit!)
* You can resize your cluster with no downtime (thanks to Membase's built in support and rebalancing ability)


Things to do after stack creation:
==================================
* Adjust the security policy (or update the template to reflect that). The current security policy will allow anyone access. Alternatively, you can create a secure bucket (using SASL).
* If you have created a default bucket you MUST update your security policy since the default security allows everyone access and the default bucket created with this template is a bucket without a password.


About Membase
=============
Membase Server is a high-performance, distributed key-value store. Membase is protocol complient to memcache (http://memcached.org/) and can provide a drop-in replacement for it with the added benefits of infinite scalability with no downtime and persistency.

