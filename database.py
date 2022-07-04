import os
import json
import sqlite3
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent




# def add_raw_to_db():

items = [

    {
        'q': 'Select TRUE statements',
        'options': {'A PaaS solution that hosts web apps in Azure provides FULL CONTROL of the OS that hosts applications': None, 'A PaaS solution thats hosts web apps in Azure provides the ability to SCALE the platform automatically': True,
                    'A PaaS solution that hosts web apps in Azure provides professional development services to continuously add features to custom applications': True},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-paas/',
        'explain': """Box 1: No -
A PaaS solution does not provide access to the operating system. The Azure Web Apps service provides an environment for you to host your web applications.
Behind the scenes, the web apps are hosted on virtual machines running IIS. However, you have no direct access to the virtual machine, the operating system or
IIS.

Box 2: Yes -
A PaaS solution that hosts web apps in Azure does provide the ability to scale the platform automatically. This is known as autoscaling. Behind the scenes, the web apps are hosted on virtual machines running IIS. Autoscaling means adding more load balanced virtual machines to host the web apps.

Box 3: Yes -
PaaS provides a framework that developers can build upon to develop or customize cloud-based applications. PaaS development tools can cut the time it takes to code new apps with pre-coded application components built into the platform, such as workflow, directory services, security features, search and so on.
References:""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'multi',
        'id': 2001
    },
    {
        'q': 'Select TRUE statements',
        'options': {'Azure provides flexibility between CapEX and OpEx': True, 'If you create 2 VMs that use the B2S size, each VM will always generate the same monthly cost': None,
                    'When an Azure VM is stopped, you continue to pay storage costs accociated with the VM.': True},
        'explain_url': 'https://meritsolutions.com/capex-vs-opex-cloud-computing-blog/',
        'explain': """Box 1: Yes -
Traditionally, IT expenses have been considered a Capital Expenditure (CapEx). Today, with the move to the cloud and the pay-as-you-go model, organizations have the ability to stretch their budgets and are shifting their IT CapEx costs to Operating Expenditures (OpEx) instead. This flexibility, in accounting terms, is now an option due to the as a Service model of purchasing software, cloud storage and other IT related resources.

Box 2: No -
Two virtual machines using the same size could have different disk configurations. Therefore, the monthly costs could be different.

Box 3: Yes -
When an Azure virtual machine is stopped, you don't pay for the virtual machine. However, you do still pay for the storage costs associated to the virtual machine.
The most common storage costs are for the disks attached to the virtual machines. There are also other storage costs associated with a virtual machine such as storage for diagnostic data and virtual machine backups.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'multi',
        'id': 2002
    },
    {
        'q': 'When you implement a SaaS solution, your are responsible for:',
        'options': {'Configuring High Availability': None, 'Defining scalability rules': None,
                    'Installing the SaaS solution': None, 'Configuring the SaaS solution': True},
        'explain_url': 'https://azure.microsoft.com/en-in/overview/what-is-saas/',
        'explain': """When you are implementing a Software as a Service (SaaS) solution, you are responsible for configuring the SaaS solution. Everything else is managed by the cloud provider.

SaaS requires the least amount of management. The cloud provider is responsible for managing everything, and the end user just uses the software.
Software as a service (SaaS) allows users to connect to and use cloud-based apps over the Internet. Common examples are email, calendaring and office tools (such as Microsoft Office 365).

SaaS provides a complete software solution which you purchase on a pay-as-you-go basis from a cloud service provider. You rent the use of an app for your organization and your users connect to it over the Internet, usually with a web browser. All of the underlying infrastructure, middleware, app software and app data are located in the service providers data center. The service provider manages the hardware and software and with the appropriate service agreement, will ensure the availability and the security of the app and your data as well.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2003
    },
    {
        'q': """You have an on-premises network that contains several servers.
You plan to migrate all the servers to Azure.
You need to recommend a solution to ensure that some of the servers are available if a single Azure data center goes offline for an extended period.
What should you include in the recommendation?""",
        'options': {'fault tolerance': True, 'elasticity': None,
                    'scalability': None, 'low latency': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machines/windows/manage-availability',
        'explain': """Fault tolerance is the ability of a system to continue to function in the event of a failure of some of its components.
In this question, you could have servers that are replicated across datacenters.

Availability zones expand the level of control you have to maintain the availability of the applications and data on your VMs. Availability Zones are unique physical locations within an Azure region. Each zone is made up of one or more datacenters equipped with independent power, cooling, and networking. To ensure resiliency, there are a minimum of three separate zones in all enabled regions. The physical separation of Availability Zones within a region protects applications and data from datacenter failures.

With Availability Zones, Azure offers industry best 99.99% VM uptime SLA. By architecting your solutions to use replicated VMs in zones, you can protect your applications and data from the loss of a datacenter. If one zone is compromised, then replicated apps and data are instantly available in another zone.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2004
    },
    {
        'q': """An organization that hosts its infrastructure __________ no longer requires a data center""",
        'options': {'in a private cloud': None, 'in a hybrid cloud': None,
                    'in the public cloud': True, 'on a Hyper-V host': None},
        'explain_url': 'https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/4-cloud-deployment-models',
        'explain': """A private cloud is hosted in your datacenter. Therefore, you cannot close your datacenter if you are using a private cloud.
A public cloud is hosted externally, for example, in Microsoft Azure. An organization that hosts its infrastructure in a public cloud can close its data center.

Public cloud is the most common deployment model. In this case, you have no local hardware to manage or keep up-to-date everything runs on your cloud provider's hardware.
Microsoft Azure is an example of a public cloud provider.

In a private cloud, you create a cloud environment in your own datacenter and provide self-service access to compute resources to users in your organization.
This offers a simulation of a public cloud to your users, but you remain completely responsible for the purchase and maintenance of the hardware and software services you provide.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2005
    },
    {
        'q': 'What are two characteristics of the public cloud? Each correct answer presents a complete solution.',
        'options': {' dedicated hardware': None, 'unsecured connections': True,
                    ' limited storage': None, 'metered pricing': True, 'self-service management': True},
        'explain_url': 'https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/4-cloud-deployment-models',
        'explain': """With the public cloud, you get pay-as-you-go pricing you pay only for what you use, no CapEx costs.
        
With the public cloud, you have self-service management. You are responsible for the deployment and configuration of the cloud resources such as virtual machines or web sites. The underlying hardware that hosts the cloud resources is managed by the cloud provider.

Incorrect Answers:
A: You don't have dedicated hardware. The underlying hardware is shared so you could have multiple customers using cloud resources hosted on the same physical hardware.

B: Connections to the public cloud are secure.

C: Storage is not limited. You can have as much storage as you like.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'multi',
        'id': 2006
    },
    {
        'q': 'Fill in the blank.  When planning to migrate a public website to Azure, you must plan to',
        'options': {'deploy a VPN': None, 'pay a monthly usage cost': True,
                    'pay to transfer all the website data to Azure': None, 'reduce the number of connections to the website': None},
        'explain_url': '',
        'explain': 'When planning to migrate a public website to Azure, you must plan to pay monthly usage costs. This is because Azure uses the pay-as-you-go model.',
        'notes': '',
        'history': '',
        'category': '',
        'q_type': 'basic',
        'id': 2007
    },
    {
        'q': """Your company plans to migrate all its data and resources to Azure.
The company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure.
You need to deploy an Azure environment that meets the company migration plan.
Solution: You create an Azure App Service and Azure SQL databases.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': '',
        'explain': 'Azure App Service and Azure SQL databases are examples of Azure PaaS solutions. Therefore, this solution does meet the goal.',
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2008
    },
    {
        'q': """Your company plans to migrate all its data and resources to Azure.
The company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure.
You need to deploy an Azure environment that meets the company migration plan.
Solution: You create an Azure App Service and Azure virtual machines that have Microsoft SQL Server installed.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': '',
        'explain': 'Azure App Service is a PaaS (Platform as a Service) service. However, Azure virtual machines are an IaaS (Infrastructure as a Service) service. Therefore, this solution does not meet the goal.',
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2009
    },
    {
        'q': """Your company plans to migrate all its data and resources to Azure.
The company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure.
You need to deploy an Azure environment that meets the company migration plan.
Solution: You create an Azure App Service and Azure Storage accounts.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': '',
        'explain': 'Azure App Service is a PaaS (Platform as a Service) service. However, Azure Storage accounts are an IaaS (Infrastructure as a Service) service. Therefore, this solution does not meet the goal.',
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2010
    },{
        'q': """Your company hosts an accounting application named App1 that is used by all the customers of the company.
App1 has low usage during the first three weeks of each month and very high usage during the last week of each month.
Which benefit of Azure Cloud Services supports cost management for this type of usage pattern?""",
        'options': {'high availability': None, 'high latency': None,
                    'elasticity': True, 'load balancing': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-elastic-computing/',
        'explain': """Elasticity in this case is the ability to provide additional compute resource when needed and reduce the compute resource when not needed to reduce costs.

Autoscaling is an example of elasticity.

Elastic computing is the ability to quickly expand or decrease computer processing, memory and storage resources to meet changing demands without worrying about capacity planning and engineering for peak usage. Typically controlled by system monitoring tools, elastic computing matches the amount of resources allocated to the amount of resources actually needed without disrupting operations. 

With cloud elasticity, a company avoids paying for unused capacity or idle resources and doesn't have to worry about investing in the purchase or maintenance of additional resources and equipment.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2011
    },
    {
        'q': """You plan to migrate a web application to Azure. The web application is accessed by external users.
You need to recommend a cloud deployment solution to minimize the amount of administrative effort used to manage the web application.
What should you include in the recommendation?""",
        'options': {'Software as a Service (SaaS)': None, ' Platform as a Service (PaaS)': True,
                    'Infrastructure as a Service (IaaS)': None, 'Database as a Service (DaaS)': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-app-services',
        'explain': """Azure App Service is a platform-as-a-service (PaaS) offering that lets you create web and mobile apps for any platform or device and connect to data anywhere, in the cloud or on-premises. App Service includes the web and mobile capabilities that were previously delivered separately as Azure Websites and Azure Mobile
Services.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2012
    },
    {
        'q': '(Fill in the blank.)   ______________',
        'options': {'Azure virtual machines': 'Infrastructure as a service (IaaS)', 'Azure SQL databases': 'Platform as a service (PaaS)'},
        'explain_url': 'https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/5-types-of-cloud-services https://docs.microsoft.com/en-us/azure/sql-database/sql-database-paas-index',
        'explain': """Box 1:
Azure virtual machines are Infrastructure as a Service (IaaS).
Infrastructure as a Service is the most flexible category of cloud services. It aims to give you complete control over the hardware that runs your application (IT infrastructure servers and virtual machines (VMs), storage, networks, and operating systems). Instead of buying hardware, with IaaS, you rent it.


Box 2:
Azure SQL databases are Platform as a Service (Paas).
Azure SQL Database is a fully managed Platform as a Service (PaaS) Database Engine that handles most of the database management functions such as upgrading, patching, backups, and monitoring without user involvement. Azure SQL Database is always running on the latest stable version of SQL Server

Database Engine and patched OS with 99.99% availability. PaaS capabilities that are built-in into Azure SQL database enable you to focus on the domain specific database administration and optimization activities that are critical for your business.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'match',
        'id': 2013
    },
    {
        'q': """You have an on-premises network that contains 100 servers.
You need to recommend a solution that provides additional resources to your users. The solution must minimize capital and operational expenditure costs.
What should you include in the recommendation?""",
        'options': {'a complete migration to the public cloud': None, 'an additional data center': None,
                    'a private cloud': None, ' hybrid cloud': True},
        'explain_url': """https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/4-cloud-deployment-models""",
        'explain': """A hybrid cloud is a combination of a private cloud and a public cloud.
Capital expenditure is the spending of money up-front for infrastructure such as new servers.
With a hybrid cloud, you can continue to use the on-premises servers while adding new servers in the public cloud (Azure for example). Adding new servers in
Azure minimizes the capital expenditure costs as you are not paying for new servers as you would if you deployed new server on-premises.

Incorrect Answers:
A: A complete migration of 100 servers to the public cloud would involve a lot of operational expenditure (the cost of migrating all the servers).

B: An additional data center would involve a lot of capital expenditure (the cost of the new infrastructure).

C: A private cloud is hosted on on-premises servers to this would involve a lot of capital expenditure (the cost of the new infrastructure to host the private cloud).""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2014
    },
    {
        'q': 'Select checkbox if answer is correct',
        'options': {'To achieve a hybrid cloud model, a company must always migrate from a private cloud model': None, 'A company can extend the capacity of its internal network by using the public cloud': True,
                    'In a public cloud model, only guest users at your company can access the resources in the cloud': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-hybrid-cloud-computing/',
        'explain': """Box 1: No -
It is not true that a company must always migrate from a private cloud model to implement a hybrid cloud. You could start with a public cloud and then combine that with an on-premise infrastructure to implement a hybrid cloud.

Box 2: Yes -
A company can extend the capacity of its internal network by using the public cloud. This is very common. When you need more capacity, rather than pay out for new on-premises infrastructure, you can configure a cloud environment and connect your on-premises network to the cloud environment by using a VPN.

Box 3: No -
It is not true that only guest users can access cloud resources. You can give anyone with an account in Azure Active Directory access to the cloud resources.
There are many authentication scenarios but a common one is to replicate your on-premises Active Directory accounts to Azure Active Directory and provide access to the Azure Active Directory accounts. Another commonly used authentication method is ג€˜Federationג€™ where authentication for access to cloud resources is passed to another authentication provider such as an on-premises Active Directory.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'multi',
        'id': 2015
    },
    {
        'q': """You plan to migrate several servers from an on-premises network to Azure.
What is an advantage of using a public cloud service for the servers over an on-premises network?""",
        'options': {'The public cloud is owned by the public, NOT a private corporation': None, 'The public cloud is a crowd-sourcing solution that provides corporations with the ability to enhance the cloud': None,
                    'All public cloud resources can be freely accessed by every member of the public': None, 'The public cloud is a shared entity whereby multiple corporations each use a portion of the resources in the cloud': True},
        'explain_url': '',
        'explain': """The public cloud is a shared entity whereby multiple corporations each use a portion of the resources in the cloud. The hardware resources (servers, infrastructure etc.) are managed by the cloud provider. Multiple companies create resources such as virtual machines and virtual networks on the hardware resources.

Incorrect Answers:

A: The public cloud is not owned by the public. In the case of Microsoft Azure, the cloud is owned by Microsoft.

B: The public cloud is a not crowd-sourcing solution. In the case of Microsoft Azure, the cloud is owned by Microsoft.

C: It is not true that public cloud resources can be freely accessed by every member of the public. You pay for a cloud subscription and create accounts for your users to access your cloud resources. No one can access your cloud resources until you create user accounts and provide the appropriate access permissions.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2016
    },
    {
    'q': """Fill in the blank.  Azure Site Recovery provides ________ for virtual machines""",
    'options': {'fault tolerance': True, 'disacter recovery': None,
                     'elasticity': None, 'high availability': None},
'explain_url': 'https://docs.microsoft.com/en-us/azure/site-recovery/site-recovery-overview',
'explain': """Azure Site Recovery helps ensure business continuity by keeping business apps and workloads running during outages. Site Recovery replicates workloads running on physical and virtual machines (VMs) from a primary site to a secondary location.""",
'notes': '',
'history': '',
'category': 'concepts',
'q_type': 'basic',
'id': 2017
},
{
'q': """In which type of cloud model are all the hardware resources owned by a third-party and shared between multiple tenants?""",
     'options': {'private': None, 'hybrid': None,
                 'public': True, 'community': None},
'explain_url': '',
'explain': """Microsoft Azure, Amazon Web Services and Google Cloud are three examples of public cloud services.

Microsoft, Amazon and Google own the hardware. The tenants are the customers who use the public cloud services.""",
'notes': '',
'history': '',
'category': 'concepts',
'q_type': 'basic',
'id': 2018
},
    {
        'q': """Fill in the blank.  An Azure web app that queries an on-premises MS SQL server is an example of a  _______ cloud""",
        'options': {'hybrid': True, 'multi-vendor': None,
                    'private': None, 'public': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-hybrid-cloud-computing/',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2019
    },
    {
        'q': """You have 1,000 virtual machines hosted on the Hyper-V hosts in a data center.
You plan to migrate all the virtual machines to an Azure pay-as-you-go subscription.
You need to identify which expenditure model to use for the planned Azure solution.
Which expenditure model should you identify?""",
        'options': {'operational': True, 'elastic': None,
                    'capital': None, 'scalable': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/architecture/cloud-adoption/appendix/azure-scaffold',
        'explain': """One of the major changes that you will face when you move from on-premises cloud to the public cloud is the switch from capital expenditure (buying hardware) to operating expenditure (paying for service as you use it). 
        
        This switch also requires more careful management of your costs. The benefit of the cloud is that you can fundamentally and positively affect the cost of a service you use by merely shutting down or resizing it when it's not needed.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2020
    },
    {
        'q': """Match the best answer.""",
        'options': {'Disaster recovery': 'A cloud service that can be recovered after a failure occurs', 'Fault tolerance': 'A cloud service that remains available after a failure occurs',
                    'Dynamic scalability': 'A cloud service that preforms quickly when demand increases', 'Low latency': 'A cloud service that can be accessed quickly from the internet'},
        'explain_url': 'https://msdn.microsoft.com/en-us/magazine/mt422582.aspx',
        'explain': """Box 1:
Fault tolerance is the ability of a service to remain available after a failure of one of the components of the service. For example, a service running on multiple servers can withstand the failure of one of the servers.

Box 2:
Disaster recovery is the recovery of a service after a failure. For example, restoring a virtual machine from backup after a virtual machine failure.

Box 3:
Dynamic scalability is the ability for compute resources to be added to a service when the service is under heavy load. For example, in a virtual machine scale set, additional instances of the virtual machine are added when the existing virtual machines are under heavy load.

Box 4:
Latency is the time a service to respond to requests. For example, the time it takes for a web page to be returned from a web server. Low latency means low response time which means a quicker response.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'match',
        'id': 2021
    },
    {
        'q': """Select the true statements""",
        'options': {'TO implement a hybrid model, a company must have an internal network': None, 'A company can extend the computing resources of its internal network by using a hybrid cloud': True,
                    'In a public cloud model, only guest users at your company can access the resources in the cloud': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-hybrid-cloud-computing/',
        'explain': """Box 1: No -
It is not true that a company must always migrate from an internal network to implement a hybrid cloud. You could start with a public cloud and then combine that with an on-premise infrastructure to implement a hybrid cloud.

Box 2: Yes -
A company can extend the computing resources of its internal network by using the public cloud. This is very common. When you need more resources, rather than pay out for new on-premises infrastructure, you can configure a cloud environment and connect your on-premises network to the cloud environment by using a VPN.

Box 3: No -
It is not true that only guest users can access cloud resources. You can give anyone with an account in Azure Active Directory access to the cloud resources.

There are many authentication scenarios but a common one is to replicate your on-premises Active Directory accounts to Azure Active Directory and provide access to the Azure Active Directory accounts. Another commonly used authentication method is ג€˜Federationג€™ where authentication for access to cloud resources is passed to another authentication provider such as an on-premises Active Directory.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'multi',
        'id': 2022
    },
    {
        'q': """Select only YES items.""",
        'options': {'A PaaS solution provides full control of operating systems that host applications': None, 'A PaaS solution provides additional memory to apps by changing pricing tiers': None,
                    'A PaaS solution can automatically scale the number of instances': True},
        'explain_url': '',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2023
    },
    {
        'q': """Select all that are True.  Your company has an on-premises network that contains multiple servers.
The company plans to reduce the following administrative responsibilities of network administrators:

✑ Backing up application data
✑ Replacing failed server hardware
✑ Managing physical server security
✑ Updating server operating systems
✑ Managing permissions to shared documents

The company plans to migrate several servers to Azure virtual machines.
You need to identify which administrative responsibilities will be eliminated after the planned migration.

Which two responsibilities should you identify?""",
        'options': {'Replacing failed server hardware': True, 'Backing up application data': None,
                    'Managing physical server security': True, 'Updating server operating systems': None, 'Managing permissions to shared documents': None},
        'explain_url': '',
        'explain': """Azure virtual machines run on Hyper-V physical servers. The physical servers are owned and managed by Microsoft. As an Azure customer, you have no access to the physical servers. Microsoft manage the replacement of failed server hardware and the security of the physical servers so you dont need to Incorrect Answers:

B: Microsoft have no control over the applications you run on the virtual machines. Therefore, it is your responsibility to ensure that application data is backed up.

D: Microsoft do not manage the operating systems you run on the virtual machines. Therefore, it is your responsibility to ensure that the operating systems are updated.

E: Microsoft have no control over the shared folders you host on the virtual machines. Therefore, it is your responsibility to ensure that folder permissions are configured appropriately..""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2024
    },
    {
        'q': """Select all TRUE answers""",
        'options': {'Azure Pay-as-you-Go pricing is an example of CapEX': None, 'Paying electricity for your datacenter is an example of OpEx': True,
                    'Deploying your own datacenter is an example of CapEx': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/architecture/cloud-adoption/appendix/azure-scaffold',
        'explain': """Box 1: No -
With the pay-as-go model, you pay for services as you use them. This is Opex (Operational Expenditure), not CapEx (Captial Expenditure). CapEx is where you pay for something upfront. For example, buying a new physical server.

Box 2: Yes -
Paying for electricity for your own datacenter will be classed as CapEx, not OpEx.

Box 3: Yes -
Deploying your own datacenter is an example of CapEx. This is because you need to purchase all the infrastructure upfront before you can use it.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2025
    },
    {
        'q': """You plan to provision Infrastructure as a Service (IaaS) resources in Azure.
Which resource is an example of IaaS?""",
        'options': {'an Azure web app': None, 'an Azure virtual machine': True,
                    'an Azure logic app': None, 'an Azure SQL database': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-iaas/',
        'explain': """An Azure virtual machine is an example of Infrastructure as a Service (IaaS).
Azure web app, Azure logic app and Azure SQL database are all examples of Platform as a Service (Paas).""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2026
    },
    {
        'q': """To which cloud models can you deploy physical servers?""",
        'options': {'private cloud and hybrid cloud only': None, 'private cloud only': None,
                    'private cloud, hybrid cloud and public cloud': None, 'hybrid cloud only': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-hybrid-cloud-computing/',
        'explain': """A private cloud is on-premises so you can deploy physical servers.
A hybrid cloud is a mix of on-premise and public cloud resources. You can deploy physical servers on-premises.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2027
    },
    {
        'q': """Select the best definition""",
        'options': {'Public Cloud': 'No required capital expenditures', 'Private Cloud': 'Provides complete control over security',
                    'Hybrid Cloud': 'Provides a choice to use on-premises or cloud-based resources'},
        'explain_url': '',
        'explain': """Box 1: Public Cloud -
With a public cloud, there is no capital expenditure on server hardware etc. You only pay for cloud resources that you use as you use them.

Box 2: Private Cloud -
A private cloud exists on premises, so you have complete control over security.

Box 3: Hybrid Cloud -
A hybrid cloud is a mix of public cloud resources and on-premises resources. Therefore, you have a choice to use either.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'match',
        'id': 2028
    },
    {
        'q': """Select correct answers only""",
        'options': {'A copany can extend a private cloud by adding its own physical servers to the public cloud': None, 'To build a hybrid cloud, you must deploy resources to the public cloud': True,
                    'A private cloud must be disconnected from the internet': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-are-private-public-hybrid-clouds/',
        'explain': """Box 1: No -
You cannot add physical servers to the public cloud. You can only deploy virtual servers in the public cloud. You can extend a private cloud by deploying virtual servers in a public cloud. This would create a hybrid cloud.

Box 2: Yes -
A hybrid cloud is a combination of a private cloud and public cloud. Therefore, to create a hybrid cloud, you must deploy resources to a public cloud.
Box 3: No.
It is not true that a private cloud must be disconnected from the Internet. Private clouds can be and most commonly are connected to the Internet. Private cloud means that the physical servers are managed by you. It does not mean that it is disconnected from the Internet.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'multi',
        'id': 2029
    },
    {
        'q': """You have 50 virtual machines hosted on-premises and 50 virtual machines hosted in Azure. The on-premises virtual machines and the Azure virtual machines connect to each other.
Which type of cloud model is this?""",
        'options': {'hybrid': True, 'private': None,
                    'public': None, 'community': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-hybrid-cloud-computing/',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2030
    },

    {
        'q': 'Select TRUE statements',
        'options': {
            'A PaaS solution that hosts web apps in Azure provides FULL CONTROL of the OS that hosts applications': None,
            'A PaaS solution thats hosts web apps in Azure provides the ability to SCALE the platform automatically': True,
            'A PaaS solution that hosts web apps in Azure provides professional development services to continuously add features to custom applications': True},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/what-is-paas/',
    'explain': """Box 1: No -
A PaaS solution does not provide access to the operating system. The Azure Web Apps service provides an environment for you to host your web applications.
Behind the scenes, the web apps are hosted on virtual machines running IIS. However, you have no direct access to the virtual machine, the operating system or
IIS.

Box 2: Yes -

Box 3: Yes -
A PaaS solution that hosts web apps in Azure does provide the ability to scale the platform automatically. This is known as autoscaling. Behind the scenes, the web apps are hosted on virtual machines running IIS. Autoscaling means adding more load balanced virtual machines to host the web apps.""",
    'notes': '',
    'history': '',
    'category': 'concepts',
    'q_type': 'multi',
    'id': 2031
},
    {
        'q': """Your company plans to migrate all its data and resources to Azure.
The companys migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure.
You need to deploy an Azure environment that meets the company migration plan.
Solution: You create Azure virtual machines, Azure SQL databases, and Azure Storage accounts.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://azure.microsoft.com/en-us/overview/what-is-paas/',
        'explain': """Platform as a service (PaaS) is a complete development and deployment environment in the cloud. PaaS includes infrastructure ג€" servers, storage, and networking ג€" but also middleware, development tools, business intelligence (BI) services, database management systems, and more. PaaS is designed to support the complete web application lifecycle: building, testing, deploying, managing, and updating.
However, virtual machines are examples of Infrastructure as a service (IaaS). IaaS is an instant computing infrastructure, provisioned and managed over the internet.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2032
    },
    {
        'q': """Your company plans to deploy several custom applications to Azure. The applications will provide invoicing services to the customers of the company. Each application will have several prerequisite applications and services installed.
You need to recommend a cloud deployment solution for all the applications.
What should you recommend?""",
        'options': {'Software as a Service (SaaS)': None, 'Platform as a Service (PaaS)': None,
                    'Infrastructure as a Service (laaS)': True},
        'explain_url': 'https://azure.microsoft.com/en-us/overview/what-is-iaas/',
        'explain': """Infrastructure as a service (IaaS) is an instant computing infrastructure, provisioned and managed over the internet. The IaaS service provider manages the infrastructure, while you purchase, install, configure, and manage your own software

Incorrect Answers:

A: Software as a service (SaaS) allows users to connect to and use cloud-based apps over the Internet. Common examples are email, calendaring, and office tools. In this scenario, you need to run your own apps, and therefore require an infrastructure.

B:
Platform as a service (PaaS) is a complete development and deployment environment in the cloud. PaaS includes infrastructureג€"servers, storage, and networkingג€"but also middleware, development tools, business intelligence (BI) services, database management systems, and more. PaaS is designed to support the complete web application lifecycle: building, testing, deploying, managing, and updating.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2033
    },
    {
        'q': """Select only True statements""",
        'options': {'Building a datacenter infrastructure is an example of OpEx': None, 'Monthly salaries for technical personnel is an example of of OpEx': True,
                    'Leasing software is an example of OpEx': True},
        'explain_url': '',
        'explain': """Box 1: No -
Building a data center infrastructure is capital expenditure, not operation expenditure.

Box 2: Yes -
OpEx is ongoing costs (costs of operations) such as staff salaries.

Box 2: Yes -
OpEx is ongoing costs (costs of operations) such as leasing software. If you purchased software as a one-off purchase, that would be CapEx, but leasing software is ongoing so its OpEx.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2034
    },
    {
        'q': """Azure Cosmos DB is an example of a _______ offering""",
        'options': {'PaaS': True, 'IaaS': None,
                    'serverless': None, 'SaaS': None},
        'explain_url': '',
        'explain': 'Azure Cosmos DB is an example of a platform as a service (PaaS) cloud database provider.',
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2035
    },
    {
        'q': 'Select only True statements',
        'options': {'With software as a service (SaaS), you must apply software updates': None, 'With infrastructure as a service (IaaS), you must install software that you want to use': True,
                    'Azure Backup is an example of a platform as a service (PaaS)': True},
        'explain_url': 'https://azure.microsoft.com/en-us/overview/what-is-saas/',
        'explain': """https://azure.microsoft.com/en-us/overview/what-is-iaas/
        
https://azure.microsoft.com/en-us/overview/what-is-paas/""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'multi',
        'id': 2036
    },
    {
        'q': """Select only True statements.""",
        'options': {'You can create a resource group inside of an other resource group': None, 'An Azure virtual machine can be in multiple resource groups': None,
                    'A resource group can contain resources from multiple Azure regions': True,},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview https://www.codeisahighway.com/effective-ways-to-delete-resources-in-a-resource-group-on-azure/',
        'explain': """Box 1: No -

Box 2: No -
Each resource can exist in only one resource group.

Box 3: Yes -
Resources from multiple different regions can be placed in a resource group. The resource group only contains metadata about the resources it contains.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2037
    },
    {
        'q': """Select only True statements""",
        'options': {'MS SQL Server 2019 installed on an Azure VM is an example of a PaaS': None, 'Azure SQL Database is an example of a PaaS': True,
                    'Azure Cosmos DB is an example of a SaaS': True},
        'explain_url': '',
        'explain': """https://docs.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview 
        
        https://www.red-gate.com/simple-talk/cloud/azure/overview-of-azure-cosmos-db""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2038
    },
    {
        'q': """Fill in the blank. A MS SQL Server database that is hosted in the cloud and has software updates managed by Azure is an example of ____________""",
        'options': {'DRaaS': None, 'IaaS': None,
                    'PaaS': True, 'SaaS': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2039
    },
    {
        'q': """Your company plans to migrate all its data and resources to Azure.
The companys migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure.
You need to deploy an Azure environment that meets the companys migration plan.
What should you create?""",
        'options': {'Azure virtual machines, Azure SQL databases, and Azure Storage accounts.': None, 'an Azure App Service and Azure virtual machines that have Microsoft SQL Server installed.': None,
                    'an Azure App Service and Azure SQL databases.': True, 'Azure storage account and web server in Azure virtual machines.': None},
        'explain_url': '',
        'explain': """Azure App Service and Azure SQL databases are examples of Azure PaaS solutions. Therefore, this solution does meet the goal.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2040
    },
    {
        'q': """Fill in the blank.  You plan to deploy 20 VMs to an Azure environment. To ensure that the VM named VM1 cannot connect to other VMs, VM1 must _________""",
        'options': {'be deployed to a separate virtual network': True, 'run a different OS than the other VMs': None,
                    'be deployed to a separate resource group': None, 'have 2 NICs': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview',
        'explain': """Azure automatically routes traffic between subnets in a virtual network. Therefore, all virtual machines in a virtual network can connect to the other virtual machines in the same virtual network. Even if the virtual machines are on separate subnets within the virtual network, they can still communicate with each other.

To ensure that a virtual machine cannot connect to the other virtual machines, the virtual machine must be deployed to a separate virtual network.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2041
    },
    {
        'q': """Fill in the blank.  When you need to delegate permissions to several Azure virtual machines simultaneously, you must deploy the Azure VMs _________""",
        'options': {'to the same Azure region': None, 'by using the same Azure Resource Manager template': None,
                    'to the same resource group': True, 'to the same availability zone': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups',
        'explain': """A resource group is a logical container for Azure resources. Resource groups make the management of Azure resources easier.

With a resource group, you can allow a user to manage all resources in the resource group, such as virtual machines, websites, and subnets. The permissions you apply to the resource group apply to all resources contained in the resource group

https://docs.microsoft.com/en-us/azure/role-based-access-control/overview.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2042
    },
    {
        'q': """After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.
You plan to deploy several Azure virtual machines.
You need to ensure that the services running on the virtual machines are available if a single data center fails.

Solution: You deploy the virtual machines to two or more availability zones.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability',
        'explain': """Availability zones expand the level of control you have to maintain the availability of the applications and data on your VMs. 
        
        An Availability Zone is a physically separate zone, within an Azure region. There are three Availability Zones per supported Azure region.
Each Availability Zone has a distinct power source, network, and cooling. 

By architecting your solutions to use replicated VMs in zones, you can protect your apps and data from the loss of a datacenter. If one zone is compromised, then replicated apps and data are instantly available in another zone.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2043
    },
    {
        'q': """One of the benefits of Azure SQL Data Warehouse is that high availability is built into the platform.
Instructions: Review the underlined text. If it makes the statement correct, select ג€No change is needed. If the statement is incorrect, select the answer choice that makes the statement correct.""",
        'options': {'No change is needed': True, 'automatic scaling': None,
                    'data compression': None, 'versioning': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/sql-data-warehouse/sql-data-warehouse-overview-faq',
        'explain': """Azure Data Warehouse (now known as Azure Synapse Analytics) is a PaaS offering from Microsoft. As with all PaaS services from Microsoft, SQL Data

Warehouse offers an availability SLA of 99.9%. Microsoft can offer 99.9% availability because it has high availability features built into the platform.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2044
    },
    {
        'q': """After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You plan to deploy several Azure virtual machines.

You need to ensure that the services running on the virtual machines are available if a single data center fails.
Solution: You deploy the virtual machines to two or more regions.

Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machines/windows/regions',
        'explain': """By deploying the virtual machines to two or more regions, you are deploying the virtual machines to multiple datacenters. This will ensure that the services running on the virtual machines are available if a single data center fails.

Azure operates in multiple datacenters around the world. These datacenters are grouped in to geographic regions, giving you flexibility in choosing where to build your applications.

You create Azure resources in defined geographic regions like 'West US', 'North Europe', or 'Southeast Asia'. You can review the list of regions and their locations.

Within each region, multiple datacenters exist to provide for redundancy and availability.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2045
    },
    {
        'q': """Select only True statements""",
        'options': {'Azure resources can only access other resources in the same resource group': None, 'If you delete a resource group, all the resources in the resource group will be deleted': True,
                    'A resource group can contain resources from multiple Azure regions': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview https://www.codeisahighway.com/effective-ways-to-delete-resources-in-a-resource-group-on-azure/',
        'explain': """Box 1: No -
A resource can interact with resources in other resource groups.

Box 2: Yes -
Deleting the resource group will remove the resource group as well as all the resources in that resource group. This can be useful for the management of resources. For example, a virtual machine has several components (the VM itself, virtual disks, network adapter etc.). By placing the VM in its own resource group, you can delete the VM along with all its associated components by deleting the resource group.
Another example is when creating a test environment. You could place the entire test environment (Network components, virtual machines etc.) in one resource group. You can then delete the entire test environment by deleting the resource group.

Box 3: Yes -
Resources from multiple different regions can be placed in a resource group. The resource group only contains metadata about the resources it contains.""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'basic',
        'id': 2046
    },
    {
        'q': """You plan to store 20 TB of data in Azure. The data will be accessed infrequently and visualized by using Microsoft Power BI.
You need to recommend a storage solution for the data.
Which two solutions should you recommend? Each correct answer presents a complete solution.""",
        'options': {'Azure Data Lake': None, 'Azure Cosmos DB': True,
                    'Azure SQL Data Warehouse': None, 'Azure SQL Database': None, 'Azure Database for PostgreSQL': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-power-bi',
        'explain': """You can use Power BI to analyze and visualize data stored in Azure Data Lake and Azure SQL Data Warehouse.

Azure Data Lake includes all of the capabilities required to make it easy for developers, data scientists and analysts to store data of any size and shape and at any speed, and do all types of processing and analytics across platforms and languages. It removes the complexities of ingesting and storing all your data while making it faster to get up and running with batch, streaming and interactive analytics. It also integrates seamlessly with operational stores and data warehouses so that you can extend current data applications.

https://azure.microsoft.com/en-gb/solutions/data-lake/ 

https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-power-bi
""",
        'notes': '',
        'history': '',
        'category': 'concepts',
        'q_type': 'multi',
        'id': 2047
    },
    {
        'q': 'You have an Azure environment that contains 10 web apps. To which URL should you connect to manage all the Azure resources? https://_______._______.com',
        'options': {'admin.': None, 'portal.': True, 'www.': None,
                    'azure.': True, 'azurewebsites.': None, 'microsoft.': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/features/azure-portal/',
        'explain': """The Azure portal is a web-based management interface where you can view and manage all your Azure resources in one unified hub, including web apps, databases, virtual machines, virtual networks, storage and Visual Studio team projects.
T
he URL of the Azure portal is https://portal.azure.com.""",
        'notes': '',
        'history': '',
        'category': '',
        'q_type': 'multi',
        'id': 2048
    },
    {
        'q': """You plan to extend your companys network to Azure. The network contains a VPN appliance that uses an IP address of 131.107.200.1.

You need to create an Azure resource that defines the VPN appliance in Azure.

Which Azure resource should you create? To answer, select the appropriate resource in the answer area.""",
        'options': {'Virtual network': None, 'Load balancers': None,
                    'Virtual network gateways': None, 'DNS Zones': None, 'Application gateways': None, 'local network gateways': True,
                    'Route tables': None, 'Route filters': None},
        'explain_url': '',
        'explain': """A Local Network Gateway is an object in Azure that represents your on-premise VPN device. 
        
        A Virtual Network Gateway is the VPN object at the Azure end of the
VPN. A connection is what connects the Local Network Gateway an the Virtual Network Gateway to bring up the VPN.

The local network gateway typically refers to your on-premises location. You give the site a name by which Azure can refer to it, then specify the IP address of the on-premises VPN device to which you will create a connection. You also specify the IP address prefixes that will be routed through the VPN gateway to the VPN device. The address prefixes you specify are the prefixes located on your on-premises network. If your on-premises network changes or you need to change the public IP address for the VPN device, you can easily update the values later.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2049
    },
    {
        'q': """Resource groups provide organizations with the ability to manage the compliance of Azure resources across multiple subscriptions.
Instructions: Review the underlined text. If it makes the statement correct, select ג€No change is neededג€. If the statement is incorrect, select the answer choice that makes the statement correct.""",
        'options': {'admin.': None, 'portal.': True, 'www.': None,
                    'azure.': True, 'azurewebsites.': None, 'microsoft.': None},
        'explain_url': '',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2050
    },
    {
        'q': """You plan to deploy several Azure virtual machines.
You need to ensure that the services running on the virtual machines are available if a single data center fails.
Solution: You deploy the virtual machines to two or more resource groups.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups',
        'explain': """A resource group is a logical container for Azure resources. When you create a resource group, you specify which location to create the resource group in.

However, when you create a virtual machine and place it in the resource group, the virtual machine can still be in a different location (different datacenter).

Therefore, creating multiple resource groups, even if they are in separate datacenters does not ensure that the services running on the virtual machines are available if a single data center fails.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2051
    },
    {
        'q': """You plan to deploy several Azure virtual machines.
You need to ensure that the services running on the virtual machines are available if a single data center fails.
Solution: You deploy the virtual machines to a scale set.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability',
        'explain': """This answer does not specify that the scale set will be configured across multiple data centers so this solution does not meet the goal.

Azure virtual machine scale sets let you create and manage a group of load balanced VMs. The number of VM instances can automatically increase or decrease in response to demand or a defined schedule. Scale sets provide high availability to your applications, and allow you to centrally manage, configure, and update many VMs.

Virtual machines in a scale set can be deployed across multiple update domains and fault domains to maximize availability and resilience to outages due to data center outages, and planned or unplanned maintenance events.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2052
    },
    {
        'q': """Select all True statements""",
        'options': {'An Azure subscription can be associated to multiple Azure Active Directory tenants.': None, 'You can change the Azure Active Directory tenant to which an Azure subscription is associated.': True,
                    'When an Azure subscription expires, the associated Azure Active Directory tenant is deleted automatically.': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory',
        'explain': """Box 1: No -
An Azure AD tenant can have multiple subscriptions but an Azure subscription can only be associated with one Azure AD tenant.

Box 2: Yes -

Box 3: No -
If your subscription expires, you lose access to all the other resources associated with the subscription. However, the Azure AD directory remains in Azure. You can associate and manage the directory using a different Azure subscription.
References:""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2053
    },
    {
        'q': """Resource groups provide organizations with the ability to manage the compliance of Azure resources across multiple subscriptions.
Instructions: Review the underlined text. If it makes the statement correct, select ג€No change is neededג€. If the statement is incorrect, select the answer choice that makes the statement correct.""",
        'options': {'No change is needed': None, 'Management groups': None,
                    'Azure policies': True, 'Azure App Service plans': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/policy/overview',
        'explain': """Azure policies can be used to define requirements for resource properties during deployment and for already existing resources. Azure Policy controls properties such as the types or locations of resources.

Azure Policy is a service in Azure that you use to create, assign, and manage policies. These policies enforce different rules and effects over your resources, so those resources stay compliant with your corporate standards and service level agreements. Azure Policy meets this need by evaluating your resources for non- compliance with assigned policies. All data stored by Azure Policy is encrypted at rest.

For example, you can have a policy to allow only a certain SKU size of virtual machines in your environment. Once this policy is implemented, new and existing resources are evaluated for compliance. With the right type of policy, existing resources can be brought into compliance.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2054
    },
    {
        'q': """Your company plans to migrate to Azure. The company has several departments. All the Azure resources used by each department will be managed by a department administrator.
What are two possible techniques to segment Azure for the departments? Each correct answer presents a complete solution.""",
        'options': {' multiple subscriptions': True, 'multiple Azure Active Directory (Azure AD) directories': None,
                    'multiple regions': None, 'multiple resource groups': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription',
        'explain': """An Azure subscription is a container for Azure resources. It is also a boundary for permissions to resources and for billing. You are charged monthly for all resources in a subscription. A single Azure tenant (Azure Active Directory) can contain multiple Azure subscriptions.

A resource group is a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution, or only those resources that you want to manage as a group.

To enable each department administrator to manage the Azure resources used by that department, you will need to create a separate subscription per department. You can then assign each department administrator as an administrator for the subscription to enable them to manage all resources in that subscription

 https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/add-change-subscription-administrator.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'mutli',
        'id': 2055
    },
    {
        'q': """Select all True statements""",
        'options': {'A single MS account can be used to manage multiple Azure subscriptions': True, 'Two Azure subscriptions can be merged into a single subscription': None,
                    'A company can use resources frommultiple subscriptions': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription',
        'explain': """Box 1: Yes -
You can use the same account to manage multiple subscriptions. You can create an additional subscription for your account in the Azure portal. You may want an additional subscription to avoid hitting subscription limits, to create separate environments for security, or to isolate data for compliance reasons.

Box 2: No -
You cannot merge two subscriptions into a single subscription. However, you can move some Azure resources from one subscription to another. You can also transfer ownership of a subscription and change the billing type for a subscription.

Box 3: Yes -
A company can have multiple subscriptions and store resources in the different subscriptions. However, a resource instance can exist in only one subscription.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2056
    },
    {
        'q': """You have several VMs in an Azure subscription.  You create a new subscription""",
        'options': {'The VMs cannot be moved to the new subscription': None, 'The VMs can be moved to the new subscription': True,
                    'The VMs can be moved to the new subscription only if they are all in the same resourse group': None, 'The VMs can be moved to the new subscription only if they run Windows Server 2016': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machines/windows/move-vm',
        'explain': """You can move a VM and its associated resources to a different subscription by using the Azure portal.

Moving between subscriptions can be handy if you originally created a VM in a personal subscription and now want to move it to your company's subscription to continue your work. You do not need to start the VM in order to move it and it should continue to run during the move.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2057
    },
    {
        'q': """You have an Azure environment that contains multiple Azure virtual machines.
You plan to implement a solution that enables the client computers on your on-premises network to communicate to the Azure virtual machines.
You need to recommend which Azure resources must be created for the planned solution.

Which two Azure resources should you include in the recommendation?""",
        'options': {'a virtual network gateway': None, ' a load balancer': None,
                    'an application gateway': True, 'a virtual network': None, 'a gateway subnet': None},
        'explain_url': 'https://docs.microsoft.com/en-us/office365/enterprise/connect-an-on-premises-network-to-a-microsoft-azure-virtual-network',
        'explain': """To implement a solution that enables the client computers on your on-premises network to communicate to the Azure virtual machines, you need to configure a

VPN (Virtual Private Network) to connect the on-premises network to the Azure virtual network.

The Azure VPN device is known as a Virtual Network Gateway. The virtual network gateway needs to be located in a dedicated subnet in the Azure virtual network. This dedicated subnet is known as a gateway subnet and must be named GatewaySubnet. Note: a virtual network (answer D) is also required. However, as we already have virtual machines deployed in a Azure, we can assume that the virtual network is already in place.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2058
    },
    {
        'q': """You attempt to create several managed Microsoft SQL Server instances in an Azure environment and receive a message that you must increase your Azure subscription limits.
What should you do to increase the limits?""",
        'options': {'Create a service health alert': None, 'Upgrade your support plan': None,
                    'Modify an Azure policy': None, 'Create a new support request': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/sql-database/sql-database-managed-instance-resource-limits#obtaining-a-larger-quota-for-sql-managed-instance',
        'explain': """Many Azure resource have quote limits. The purpose of the quota limits is to help you control your Azure costs. However, it is common to require an increase to the default quota.

You can request a quota limit increase by opening a support request. In the support request, select ג€˜Service and subscription limits (quotas)ג€™ for the Issue type, select your subscription and the service you want to increase the quota for. For this question, you would select ג€˜SQL Database Managed Instance as the quote type""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2059
    },
    {
        'q': """Select all True statements""",
        'options': {'Each Azure subscription can contain multiple account administrators': True, 'Each Azure subscription can be managed by using a Microsoft account only': None,
                    'A Azure resource group contains multiple Azure subscriptions': None},
        'explain_url': '',
        'explain': """Box 1: Yes -
You can assign additional account administrators in the Azure Portal.

Box 2: No -
You need an Azure Active Directory account to manage a subscription, not a Microsoft account.
An account is created in the Azure Active Directory when you create the subscription. Further accounts can be created in the Azure Active Directory to manage the subscription.

Box 3: No -
Resource groups are logical containers for Azure resources. However, resource groups do not contain subscriptions. Subscriptions contain resource groups.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2060
    },
    {
        'q': """Select all True statements""",
        'options': {'Availability Zones can be implemented in all Azure regions.': None, 'Only virtual machines that run Windows Server can be created in availablity zones': None,
                    'Availability Zones are used to replicate data and applications to multiple regions': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/availability-zones/az-region#azure-regions-with-availability-zones',
        'explain': """Box 1: No -
Not all Azure regions support availability zones.

Box 2: No -
Availability zones can be used with many Azure services, not just VMs.

Box 3: No -
Availability Zones are unique physical locations within a single Azure region.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2061
    },
    {
        'q': """You need to identify which storage service must be used to store the unmanaged data disks of the virtual machine.

What should you identify?""",
        'options': {'Containers': True, 'File shares': None,
                    'Tables': None, 'Queues': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-pageblob-overview',
        'explain': """Azure containers are the backbone of the virtual disks platform for Azure IaaS. Both Azure OS and data disks are implemented as virtual disks where data is durably persisted in the Azure Storage platform and then delivered to the virtual machines for maximum performance. Azure Disks are persisted in Hyper-V VHD format and stored as a page blob in Azure Storage.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2062
    },
    {
        'q': """Your company plans to move several servers to Azure.
The company's compliance policy states that a server named FinServer must be on a separate network segment.
You are evaluating which Azure services can be used to meet the compliance policy requirements.
Which Azure solution should you recommend?""",
        'options': {'a resource group for FinServer and another resource group for all the other servers': None, 'a virtual network for FinServer and another virtual network for all the other servers': True,
                    'a VPN for FinServer and a virtual network gateway for each other server': None, 'one resource group for all the servers and a resource lock for FinServer': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-vnet-plan-design-arm',
        'explain': """Networks in Azure are known as virtual networks. A virtual network can have multiple IP address spaces and multiple subnets. Azure automatically routes traffic between different subnets within a virtual network.

The question states that FinServer must be on a separate network segment. The only way to separate FinServer from the other servers in networking terms is to place the server in a different virtual network to the other servers.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2063
    },
    {
        'q': """You plan to map a network drive from several computers that run Windows 10 to Azure Storage.
You need to create a storage solution in Azure for the planned mapped drive.
What should you create?""",
        'options': {'an Azure SQL database': None, 'a virtual machine data disk': None,
                    'a Files service in a storage account': True, 'a Blobs service in a storage account': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/storage/files/storage-how-to-use-files-windows',
        'explain': """Azure Files is Microsoft's easy-to-use cloud file system. Azure file shares can be seamlessly used in Windows and Windows Server.

To use an Azure file share with Windows, you must either mount it, which means assigning it a drive letter or mount point path, or access it via its UNC path.

Unlike other SMB shares you may have interacted with, such as those hosted on a Windows Server, Linux Samba server, or NAS device, Azure file shares do not currently support Kerberos authentication with your Active Directory (AD) or Azure Active Directory (AAD) identity, although this is a feature we are working on.

Instead, you must access your Azure file share with the storage account key for the storage account containing your Azure file share. A storage account key is an administrator key for a storage account, including administrator permissions to all files and folders within the file share you're accessing, and for all file shares and other storage resources (blobs, queues, tables, etc) contained within your storage account.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2064
    },
    {
        'q': """You plan to implement an Azure database solution.
You need to implement a database solution that meets the following requirements:
✑ Can add data concurrently from multiple regions
✑ Can store JSON documents
Which database service should you deploy?""",
        'options': {'Azure Cosmos DB': True, 'SQL databases': None,
                    'Azure Database for MySQL': None, 'Azure Database for MariaDB': None}, 'SQL Data warehouse': None, 'SQL managed instance': None, 'SQL SQL servers': None,
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cosmos-db/introduction ',
        'explain': """Azure Cosmos DB is Microsoft's globally distributed, multi-model database service. With a click of a button, Cosmos DB enables you to elastically and independently scale throughput and storage across any number of Azure regions worldwide.

Azure Cosmos DB is a great way to store unstructured and JSON data. Combined with Azure Functions, Cosmos DB makes storing data quick and easy with much less code than required for storing data in a relational database

https://docs.microsoft.com/en-us/azure/azure-functions/functions-integrate-store-unstructured-data-cosmosdb?tabs=csharp.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2065
    },
    {
        'q': """Your company plans to migrate all its network resources to Azure.
You need to start the planning process by exploring Azure.
What should you create first?""",
        'options': {'a subscription': True, 'a resource group': None,
                    'a virtual network': None, ' a management group': None},
        'explain_url': 'https://docs.microsoft.com/en-us/office365/enterprise/subscriptions-licenses-accounts-and-tenants-for-microsoft-cloud-offerings',
        'explain': """The first thing you create in Azure is a subscription. You can think of an Azure subscription as an ג€˜Azure accountג€™. You get billed per subscription.

A subscription is an agreement with Microsoft to use one or more Microsoft cloud platforms or services, for which charges accrue based on either a per-user license fee or on cloud-based resource consumption.

Microsoft's Software as a Service (SaaS)-based cloud offerings (Office 365, Intune/EMS, and Dynamics 365) charge per-user license fees.

Microsoft's Platform as a Service (PaaS) and Infrastructure as a Service (IaaS) cloud offerings (Azure) charge based on cloud resource consumption.

You can also use a trial subscription, but the subscription expires after a specific amount of time or consumption charges. You can convert a trial subscription to a paid subscription.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2066
    },
    {
        'q': """Select all True statements""",
        'options': {'All the Azure resources deployed to a resource group must use the same Azure region': None, 'If you assign a tag to a resource group, all the Azure resources in that resource group are assigned the same tag': None,
                    'If you assign permissions for a user to manage the resource group, the user can manage all the Azure resources in that resource group': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview',
        'explain': """Box 1: No -
Azure resources deployed to a single resource group can be located in different regions. The resource group only contains metadata about the resources it contains.

When creating a resource group, you need to provide a location for that resource group. You may be wondering, "Why does a resource group need a location?

And, if the resources can have different locations than the resource group, why does the resource group location matter at all?" The resource group stores metadata about the resources. When you specify a location for the resource group, you're specifying where that metadata is stored. For compliance reasons, you may need to ensure that your data is stored in a particular region.

Box 2: No -
Tags for Resources are not inherited by default from their Resource Group

Box 3: Yes -
A resource group can be used to scope access control for administrative actions. By default, permissions set at the resource level are inherited by the resources in the resource group.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2067
    },
    {
        'q': """Fill in the blank.  Data that is stored in the Archive access tyier of an Azure Storage account_______________""",
        'options': {'can be accessed at any time by using azcopy.exe': None, 'can only be read by using Azure Backup': None,
                    'must be restored before the data can be accessed': None, 'must be rehydrated before the data can be accessed': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-storage-tiers?tabs=azure-portal#archive-access-tier',
        'explain': """Azure storage offers different access tiers: hot, cool and archive.

The archive access tier has the lowest storage cost. But it has higher data retrieval costs compared to the hot and cool tiers. Data in the archive tier can take several hours to retrieve.

While a blob is in archive storage, the blob data is offline and can't be read, overwritten, or modified. To read or download a blob in archive, you must first rehydrate it to an online tier.

Example usage scenarios for the archive access tier include:
✑ Long-term backup, secondary backup, and archival datasets
✑ Original (raw) data that must be preserved, even after it has been processed into final usable form.
✑ Compliance and archival data that needs to be stored for a long time and is hardly ever accessed.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2068
    },
    {
        'q': """Matching. You plan to deploy a critical line-of-business application to Azure.
The application will run on an Azure virtual machine.

You need to recommend a deployment solution for the application. The solution must provide a guaranteed availability of 99.99 percent.

What is the minimum number of virtual machines and the minimum number of availability zones you should recommend for the deployment?""",
        'options': {'Minimum number of virtual machines': '2', 'Minimum number of availability zones': '2',
                    'Minimum number of subscriptions': '1', 'Typical number of availability zones in a region': '3'},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/availability-zones/az-overview',
        'explain': """You need a minimum of two virtual machines with each one located in a different availability zone.

Availability Zones is a high-availability offering that protects your applications and data from datacenter failures. Availability Zones are unique physical locations within an Azure region. Each zone is made up of one or more datacenters equipped with independent power, cooling, and networking. 

To ensure resiliency, theres a minimum of three separate zones in all enabled regions. The physical separation of Availability Zones within a region protects applications and data from datacenter failures. Zone-redundant services replicate your applications and data across Availability Zones to protect from single-points-of-failure. With Availability
Zones, Azure offers industry best 99.99% VM uptime SLA.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2069
    },
    {
        'q': """Which Azure service should you use to collect events from multiple resources into a centralized repository?""",
        'options': {'Azure Event Hubs': None, 'Azure Analysis Services': None,
                    'Azure Monitor': True, 'Azure Stream Analytics': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-about',
        'explain': """Azure Event Hubs is a big data streaming platform and event ingestion service. It can receive and process millions of events per second. Data sent to an event hub can be transformed and stored by using any real-time analytics provider or batching/storage adapters.

Azure Event Hubs can be used to ingest, buffer, store, and process your stream in real time to get actionable insights. Event Hubs uses a partitioned consumer model, enabling multiple applications to process the stream concurrently and letting you control the speed of processing.

Azure Event Hubs can be used to capture your data in near-real time in an Azure Blob storage or Azure Data Lake Storage for long-term retention or micro-batch processing.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2070
    },
    {
        'q': """An availability Zone in Azure has physically separate locations _________""",
        'options': {'across two continents': None, 'within a single Azure region': True,
                    'within multiple Azure region': None, 'within a single Azure datacenter': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/availability-zones/az-overview',
        'explain': """Availability Zones is a high-availability offering that protects your applications and data from datacenter failures. Availability Zones are unique physical locations within an Azure region.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2071
    },
    {
        'q': """Select all True statements""",
        'options': {'Data that is stored in a Azure Storage account automatically has 3 copies': True, 'All data that is copied TO an Azure Storage account is backed up automatically to another Azure datacenter': None,
                    'An Azure Storage account can contain up to 2 TB of data and up to 1 million files': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview',
        'explain': """Box 1: Yes -
There are different replication options available with a storage account. The minimum replication option is Locally Redundant Storage (LRS). With LRS, data is replicated synchronously three times within the primary region.

Box 2: No -
Data is not backed up automatically to another Azure Data Center although it can be depending on the replication option configured for the account. Locally
Redundant Storage (LRS) is the default which maintains three copies of the data in the data center.
Geo-redundant storage (GRS) has cross-regional replication to protect against regional outages. Data is replicated synchronously three times in the primary region, then replicated asynchronously to the secondary region.

Box 3: No -
The limits are much higher than that. The current storage limit is 2 PB for US and Europe, and 500 TB for all other regions (including the UK) with no limit on the number of files.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2072
    },
    {
        'q': """Select all True statements""",
        'options': {'If you have Azure resources deployed to every region, you can implement availability zones in all the regions': None, 'Only virtual machines that run Windows Server can be created in availability zones': None,
                    'Availability zones are used to replicate data and applications to multipke regions': None},
        'explain_url': 'https://docs.microsoft.com/en-gb/azure/availability-zones/az-overview',
        'explain': """Box 1: No -
Not all Azure regions support availability zones.

Box 2: No -
Regions that support availability zones support Linux virtual machines.

Box 3: Yes -
Availability Zones is a high-availability offering that protects your applications and data from datacenter failures. Availability Zones are unique physical locations within an Azure region. Each zone is made up of one or more datacenters equipped with independent power, cooling, and networking. To ensure resiliency, thereג€™s a minimum of three separate zones in all enabled regions. The physical separation of Availability Zones within a region protects applications and data from datacenter failures. Zone-redundant services replicate your applications and data across Availability Zones to protect from single-points-of-failure. With Availability
Zones, Azure offers industry best 99.99% VM uptime SLA.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2073
    },
    {
        'q': """Select all True statements""",
        'options': {'North America is represented by a single Azure region': None, 'Every Azure region has multiple datacenters': True,
                    'Data transfers between Azure services located in different Azure regions are always free': None},
        'explain_url': 'https://azure.microsoft.com/en-us/global-infrastructure/regions/',
        'explain': """Box 1: No -
North America has several Azure regions, including West US, Central US, South Central US, East Us, and Canada East.

Box 2: Yes -
A region is a set of datacenters deployed within a latency-defined perimeter and connected through a dedicated regional low-latency network.

Box 3: No -
Outbound data transfer is charged at the normal rate and inbound data transfer is free.

https://azure.microsoft.com/en-us/pricing/details/bandwidth/""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2074
    },
    {
        'q': """You plan to deploy several Azure virtual machines.
You need to ensure that the services running on the virtual machines are available if a single data center fails.
Solution: You deploy the virtual machines to two or more scale sets.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability',
        'explain': """This answer does not specify that the scale set will be configured across multiple data centers so this solution does not meet the goal.

Azure virtual machine scale sets let you create and manage a group of load balanced VMs. The number of VM instances can automatically increase or decrease in response to demand or a defined schedule. Scale sets provide high availability to your applications, and allow you to centrally manage, configure, and update many VMs.

Virtual machines in a scale set can be deployed across multiple update domains and fault domains to maximize availability and resilience to outages due to data center outages, and planned or unplanned maintenance events.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2075
    },
    {
        'q': """You need to be notified when Microsoft plans to perform maintenance that can affect the resources deployed to an Azure subscription.
What should you use?""",
        'options': {'Azure Monitor': None, 'Azure Service Health': True,
                    'Azure Advisor': None, 'Microsoft Trust Center': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/service-health/overview',
        'explain': """Azure Service Health provides a personalized view of the health of the Azure services and regions you're using. This is the best place to look for service impacting communications about outages, planned maintenance activities, and other health advisories because the authenticated Service Health experience knows which services and resources you currently use.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2076
    },
    {
        'q': """Matching""",
        'options': {'IoT Hub': 'A managed service that provides bidirectional communication between IoT devices and Azure', 'IoT Central': 'A fully managed software as a service (SaaS) to connect, monitor, and manage IoT devices at scale',
                    'Azure Sphere': 'A software and hardware solution that provides communication and security features for IoT devices'},
        'explain_url': 'https://docs.microsoft.com/en-us/azure-sphere/product-overview/what-is-azure-sphere ',
        'explain': """https://docs.microsoft.com/en-us/azure/iot-hub/about-iot-hub""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2077
    },
    {
        'q': """Select all True statements""",
        'options': {'A Windows Virtual Desktop session host can run Windows 10 only': None, 'A Windows Virtual Desktop host pool that includes 20 session hosts supports a maximum of 20 simultaneous user connections': None,
                    'Windows Virtual Desktop supports desktop and app virtualization': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-desktop/overview',
        'explain': """https://docs.microsoft.com/en-us/azure/virtual-desktop/overview""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2078
    },
    {
        'q': """Fill in the blank. __________ can calculate cost savings due to reduced electricity consumption as a result of migrating on-premises MS SQL servers to Azure""",
        'options': {'The Azure Migrate: Server Assessment Tool': None, 'The Azure Total Cost of Ownership (TCO) calculator': True,
                    'The Database Migration Assistant': None, 'The pricing calculator in Azure': None},
        'explain_url': 'https://blog.abouttmc.com/azure-cloud-total-cost-of-ownership',
        'explain': """'https://blog.abouttmc.com/azure-cloud-total-cost-of-ownership'""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2079
    },
    {
        'q': """Select all True statements""",
        'options': {'You can use Availibility Zones in Azure to protect Azure VMs from a datacenter failure': None, 'You can use availability Zones in Azure to protect VMs from a region failure': True,
                    'You can use Availibility Zones in Azure to protect Azure managed disks from a datacenter failure': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machines/windows/manage-availability',
        'explain': """Availability zones expand the level of control you have to maintain the availability of the applications and data on your VMs. Availability Zones are unique physical locations within an Azure region. Each zone is made up of one or more datacenters equipped with independent power, cooling, and networking. To ensure resiliency, there are a minimum of three separate zones in all enabled regions. The physical separation of Availability Zones within a region protects applications and data from datacenter failures.

With Availability Zones, Azure offers industry best 99.99% VM uptime SLA. By architecting your solutions to use replicated VMs in zones, you can protect your applications and data from the loss of a datacenter. If one zone is compromised, then replicated apps and data are instantly available in another zone.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2080
    },
    {
        'q': """Select all True statements""",
        'options': {'An Azure subscription can have multiple account administrators': None, 'An Azure subscription can be managed by using a Microsoft account only': True,
                    'An Azure resource group can contain multiple Azure subscriptions': None},
        'explain_url': 'https://k21academy.com/microsoft-azure/az-900/az-900-azure-subscriptions/ https://azure.microsoft.com/en-us/blog/organizing-subscriptions-and-resource-groups-within-the-enterprise/',
        'explain': """Box 1: No -
A subscription can have multiple administrators, but there can only be one account administrator.

Box 2: Yes -
An Azure subscription is linked to a single account, the one that was used to create the subscription and is used for billing purposes. You can have more than one subscription.

Box 3: No -
A subscription can contain multiple resource groups but a resource group can only belong to one subscription. Resource groups can contain multiple resources.

https://azure.microsoft.com/en-us/blog/organizing-subscriptions-and-resource-groups-within-the-enterprise/""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2081
    },
    {
        'q': """An Azure region contains one or more data centers that are connected by using a low-latency network.""",
        'options': {'No change is needed': True, 'Is found in each country where Microsoft has a subsidiary office': None,
                    'Can be found in every country in Europe and the Americas only': None, 'Contains one or more data centers that are connected by using a high-latency network': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/global-infrastructure/regions/',
        'explain': """A region is a set of data centres deployed within a latency-defined perimeter and connected through a dedicated regional low-latency network.

Microsoft Azure currently has 55 regions worldwide.

Regions are divided into Availability Zones. Availability Zones are physically separate locations within an Azure region. Each Availability Zone is made up of one or more datacenters equipped with independent power, cooling, and networking.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2082
    },
    {
        'q': """Select all True statements""",
        'options': {'To use Azure Active Directory, credentials to sign in to a computer that runs Windows 10, the computer must be joined to Azure AD.': True, 'Users in Azure Acive Directory are organized by using resource groups': None,
                    'Azure Active Directory groups support dynamic membership rules': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-dynamic-membership',
        'explain': """Reference:
https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-dynamic-membership 

https://petri.com/understanding-hybrid-azure-active-directory-join""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2083
    },
    {
        'q': """You need to ensure that the services running on the virtual machines remain available if a single data center fails.
What are two possible solutions? Each correct answer presents a complete solution.""",
        'options': {'Deploy the virtual machines to two or more availability zones.': True, 'Deploy the virtual machines to two or more resource groups.': None,
                    'Deploy the virtual machines to a scale set.': None, 'Deploy the virtual machines to two or more regions.': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability',
        'explain': """Reference:
https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability 

https://docs.microsoft.com/en-us/azure/virtual-machines/windows/regions""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2084
    },
    {
        'q': """You have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1.

From Azure documentation, you have the following command that creates a virtual machine named VM1. 
✑  az vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys

You need to create VM1 in Subscription1 by using the command.

Solution: From the Azure portal, launch Azure Cloud Shell and select Bash. Run the command in Cloud Shell.

Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli',
        'explain': """The command can be run in the Azure Cloud Shell.

The Azure Cloud Shell is a free interactive shell. It has common Azure tools preinstalled and configured to use with your account.

To open the Cloud Shell, just select Try it from the upper right corner of a code block. You can also launch Cloud Shell in a separate browser tab by going to https://shell.azure.com/bash.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2085
    },
    {
        'q': """Each business unit requires 20 different Azure resources for daily operation. All the business units require the same type of Azure resources.
You need to recommend a solution to automate the creation of the Azure resources.
What should you include in the recommendations?""",
        'options': {'Azure Resource Manager templates': True, 'virtual machine scale sets': None,
                    ' the Azure API Management service': None, 'management groups': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview',
        'explain': """You can use Azure Resource Manager templates to automate the creation of the Azure resources. Deploying resource through templates is known as IaaS.

To implement infrastructure as code for your Azure solutions, use Azure Resource Manager templates. The template is a JavaScript Object Notation (JSON) file that defines the infrastructure and configuration for your project. The template uses declarative syntax, which lets you state what you intend to deploy without having to write the sequence of programming commands to create it. In the template, you specify the resources to deploy and the properties for those resources.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2086
    },
    {
        'q': """Matching""",
        'options': {'Azure Functions': 'Provides the platform for serverless code', 'Azure Databricks': 'A big data anaylsis service for machine learning',
                    'Azure Application Insights': 'Detects and diagnoses anomalies in web apps', 'Azure App Service': 'Hosts web apps'},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-databricks/what-is-azure-databricks#apache-spark-based-analytics-platform',
        'explain': """Box 1:
Azure Functions provides the platform for serverless code.

Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure.

Box 2:
Azure Databricks is a big analysis service for machine learning.
Azure Databricks is an Apache Spark-based analytics platform. The platform consists of several components including ג€˜MLibג€™. Mlib is a Machine Learning library consisting of common learning algorithms and utilities, including classification, regression, clustering, collaborative filtering, dimensionality reduction, as well as underlying optimization primitives.

Box 3:
Azure Application Insights detects and diagnoses anomalies in web apps.
Application Insights, a feature of Azure Monitor, is an extensible Application Performance Management (APM) service for developers and DevOps professionals.
Use it to monitor your live applications. It will automatically detect performance anomalies, and includes powerful analytics tools to help you diagnose issues and to understand what users actually do with your app.

Box 4:
Azure App Service hosts web apps.
Azure App Service is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. You can develop in your favorite language, be it
.NET, .NET Core, Java, Ruby, Node.js, PHP, or Python. Applications run and scale with ease on both Windows and Linux-based environments.

 https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
 """,
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2087
    },
    {
        'q': """A team of developers at your company plans to deploy, and then remove, 50 customized virtual machines each week. Thirty of the virtual machines run Windows
Server 2016 and 20 of the virtual machines run Ubuntu Linux.
You need to recommend which Azure service will minimize the administrative effort required to deploy and remove the virtual machines.
What should you recommend?""",
        'options': {'Azure Reserved Virtual Machines (VM) Instances': None, 'Azure virtual machine scale sets': None,
                    'Azure DevTest Labs': True, 'Microsoft Managed Desktop': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/lab-services/devtest-lab-overview',
        'explain': """DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates.

By using DevTest Labs, you can test the latest versions of your applications by doing the following tasks:

✑ Quickly provision Windows and Linux environments by using reusable templates and artifacts.

✑ Easily integrate your deployment pipeline with DevTest Labs to provision on-demand environments.

✑ Scale up your load testing by provisioning multiple test agents and create pre-provisioned environments for training and demos.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2088
    },
    {
        'q': """Select all True statements.  A support engineer plans to perform several Azure management tasks by using the Azure CLI.
You install the CLI on a computer.
You need to tell the support engineer which tools to use to run the CLI.
Which two tools should you instruct the support engineer to use?""",
        'options': {'Command Prompt': None, 'Azure Resource Explorer': None,
                    'Windows PowerShell': True, 'Windows Defender Firewall': None, 'Network and Sharing Center': None},
        'explain_url': 'https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest',
        'explain': """For Windows the Azure CLI is installed via an MSI, which gives you access to the CLI through the Windows Command Prompt (CMD) or PowerShell.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2089
    },
    {
        'q': """You have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system.
Solution: You use PowerShell in Azure Cloud Shell.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cloud-shell/features',
        'explain': """Azure Cloud Shell is a browser-based shell experience to manage and develop Azure resources.

Cloud Shell offers a browser-accessible, pre-configured shell experience for managing Azure resources without the overhead of installing, versioning, and maintaining a machine yourself.

Being browser-based, Azure Cloud Shell can be run on a browser from a tablet that runs the Android operating system.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2090
    },
    {
        'q': """You have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system.

Solution: You use the PowerApps portal.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://powerapps.microsoft.com/en-us/blog/introducing-powerapps-portals-powerful-low-code-websites-for-external-users/',
        'explain': """PowerApps lets you quickly build business applications with little or no code. It is not used to create Azure virtual machines. Therefore, this solution does not meet the goal.

PowerApps Portals allow organizations to create websites which can be shared with users external to their organization either anonymously or through the login provider of their choice like LinkedIn, Microsoft Account, other commercial login providers.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2091
    },
    {
        'q': """You have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system.
Solution: You use the Azure portal.

Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-portal/azure-portal-overview',
        'explain': """The Azure portal is a web-based, unified console that provides an alternative to command-line tools. With the Azure portal, you can manage your Azure subscription using a graphical user interface. You can build, manage, and monitor everything from simple web apps to complex cloud deployments. Create custom dashboards for an organized view of resources. Configure accessibility options for an optimal experience.

Being web-based, the Azure portal can be run on a browser from a tablet that runs the Android operating system.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2092
    },
    {
        'q': """Fill in the blank. _________ is an Apache Spark-based analytics service""",
        'options': {'Azure Databricks': True, 'Azure Data Factory': None,
                    'Azure DevOps': None, 'Azure HDInsight': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-databricks/what-is-azure-databricks#apache-spark-based-analytics-platform',
        'explain': """Azure Databricks is an Apache Spark-based analytics platform. The platform consists of several components including MLib.
         
         Mlib is a Machine Learning library consisting of common learning algorithms and utilities, including classification, regression, clustering, collaborative filtering, dimensionality reduction, as well as underlying optimization primitives.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2093
    },
    {
        'q': """Select all True statements""",
        'options': {'Azure Monitor can monitor the performance of on-premises computers': True, 'Azure Monitor can send alerts to Azure Active Directory security groups': True,
                    'Azure Monitor can trigger alerts based on data in the Azure Log Analytics workspace': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-monitor/overview ',
        'explain': """Box 1: Yes -
Azure Monitor maximizes the availability and performance of your applications and services by delivering a comprehensive solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments.

Box 2: Yes -
Alerts in Azure Monitor proactively notify you of critical conditions and potentially attempt to take corrective action.

Box 3: Yes -
Azure Monitor uses Target Resource, which is the scope and signals available for alerting. A target can be any Azure resource. Example targets: a virtual machine, a storage account, a virtual machine scale set, a Log Analytics workspace, or an Application Insights resource.

https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-overview""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2094
    },
    {
        'q': """Which Azure service provides a set of version control tools to manage code?""",
        'options': {'Azure Repos': True, 'Azure DevTest Labs': None,
                    'Azure Storage': None, 'Azure Cosmos DB': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/devops/repos/get-started/what-is-repos?view=azure-devops',
        'explain': """Azure Repos is a set of version control tools that you can use to manage your code.

Incorrect Answers:

B: Azure DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates. These have all the necessary tools and software that you can use to create environments.

D: Azure Cosmos DB is Microsoft's globally distributed, multi-model database service.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2095
    },
    {
        'q': """From the Azure Portal, which icon do you select to open the Azure Cloud Shell""",
        'options': {'Down arrow': None, 'Plus sign': True,
                    'Edit (pencil)': None, 'Minus sign': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cloud-shell/overview?view=azure-cli-latest',
        'explain': """You can access Azure Cloud Shell in the Azure portal by clicking the icon.

Azure Cloud Shell is an interactive, authenticated, browser-accessible shell for managing Azure resources. It provides the flexibility of choosing the shell experience that best suits the way you work, either Bash or PowerShell.

Cloud Shell enables access to a browser-based command-line experience built with Azure management tasks in mind.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2096
    },
    {
        'q': """You have a virtual machine named VM1 that runs Windows Server 2016. VM1 is in the East US Azure region.

Which Azure service should you use from the Azure portal to view service failure notifications that can affect the availability of VM1?""",
        'options': {'Azure Service Fabric': None, 'Azure Monitor': None,
                    'Azure virtual machines': True, 'Azure Advisor': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machines/maintenance-and-updates',
        'explain': """In the Azure virtual machines page in the Azure portal, there is a named Maintenance Status. This column will display service issues that could affect your virtual machine. A service failure is rare but host server maintenance that could affect your virtual machines is more common.

Azure periodically updates its platform to improve the reliability, performance, and security of the host infrastructure for virtual machines. The purpose of these updates ranges from patching software components in the hosting environment to upgrading networking components or decommissioning hardware.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2097
    },
    {
        'q': """An Azure administrator plans to run a PowerShell script that creates Azure resources.
You need to recommend which computer configuration to use to run the script.

Solution: Run the script from a computer that runs Linux and has the Azure CLI tools installed.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/powershell/scripting/components/ise/how-to-write-and-run-scripts-in-the-windows-powershell-ise?view=powershell-6',
        'explain': """A PowerShell script is a file that contains PowerShell cmdlets and code. A PowerShell script needs to be run in PowerShell.

PowerShell can now be installed on Linux. However, the question states that the computer has Azure CLI tools, not PowerShell installed. Therefore, this solution does not meet the goal.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2098
    },
    {
        'q': """An Azure administrator plans to run a PowerShell script that creates Azure resources.
You need to recommend which computer configuration to use to run the script.
Solution: Run the script from a computer that runs Chrome OS and uses Azure Cloud Shell.
Does this meet the goal?""",
         'options': {'Yes': True, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cloud-shell/quickstart-powershell',
        'explain': """A PowerShell script is a file that contains PowerShell cmdlets and code. A PowerShell script needs to be run in PowerShell.

With the Azure Cloud Shell, you can run PowerShell cmdlets and scripts in a Web browser. You log in to the Azure Portal and select the Azure Cloud Shell option.

This will open a PowerShell session in the Web browser. The Azure Cloud Shell has the necessary Azure PowerShell module installed.

Note: to run a PowerShell script in the Azure Cloud Shell, you need to change to the directory where the PowerShell script is stored.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2099
    },
    {
        'q': """Select all True statements""",
        'options': {'From Azure Service Health, an administrator can view the health of all the services inan Azure Environment': True, 'From Azure Service Health, an administrator can create a rule to be alerted if an Azure service fails': True,
                    'From Azure Service Health, an administrator can prevent a service failure': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/service-health/overview',
        'explain': """Azure Service Health consists of three components: Azure Status, Azure Service Heath and Azure Resource Health.

Azure service health provides a personalized view of the health of the Azure services and regions you're using. This is the best place to look for service impacting communications about outages, planned maintenance activities, and other health advisories because the authenticated Azure Service Health experience knows which services and resources you currently use.

To view the health of all other services available in Azure, you would use the Azure Status component of Azure Service Health. Azure status informs you of service outages in Azure on the Azure Status page. The page is a global view of the health of all Azure services across all Azure regions.

Box 2: Yes -
The best way to use Service Health is to set up Service Health alerts to notify you via your preferred communication channels when service issues, planned maintenance, or other changes may affect the Azure services and regions you use.

Box 3: No -
You can use Resource Health to view the health of a virtual machine. However, you cannot use Resource Health to prevent a service failure affecting the virtual machine.
Azure resource health provides information about the health of your individual cloud resources such as a specific virtual machine instance.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2100
    },
{
        'q': """An Azure administrator plans to run a PowerShell script that creates Azure resources.
You need to recommend which computer configuration to use to run the script.

Solution: Run the script from a computer that runs macOS and has PowerShell Core 6.0 installed.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/powershell/scripting/components/ise/how-to-write-and-run-scripts-in-the-windows-powershell-ise?view=powershell-6',
        'explain': """A PowerShell script is a file that contains PowerShell cmdlets and code. A PowerShell script needs to be run in PowerShell.

In this question, the computer has PowerShell Core 6.0 installed. Therefore, this solution does meet the goal.

Note: To create Azure resources using PowerShell, you would need to import the Azure PowerShell module which includes the PowerShell cmdlets required to create the resources.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2101
    },
    {'q': """Matching""",
        'options': {'Azure DevOps': 'An integrated solution for the deployment of code.', 'Azure Advisor': 'A tool that provides guidance and recommendations to improve an Azure environment',
                    'Azure Cognitive Services': 'A simplified tool to build Artificial Intelligence applications', 'Azure Applicaton Insights': 'Monitor web applications'},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview',
        'explain': """Box 1: Azure DevOps.
Azure DevOps is Microsofts primary software development and deployment platform.
DevOps influences the application lifecycle throughout its plan, develop, deliver and operate phases.

Box 2: Azure Advisor.
Advisor is a personalized cloud consultant that helps you follow best practices to optimize your Azure deployments. It analyzes your resource configuration and usage telemetry and then recommends solutions that can help you improve the cost effectiveness, performance, high availability, and security of your Azure resources.

Box 3: Azure Cognitive Services.
Azure Cognitive Services are APIs, SDKs, and services available to help developers build intelligent applications without having direct AI or data science skills or knowledge. Azure Cognitive Services enable developers to easily add cognitive features into their applications. The goal of Azure Cognitive Services is to help developers create applications that can see, hear, speak, understand, and even begin to reason. The catalog of services within Azure Cognitive Services can be categorized into five main pillars - Vision, Speech, Language, Web Search, and Decision.

Box 4. Azure Application Insights.
Azure Application Insights detects and diagnoses anomalies in web apps.
Application Insights, a feature of Azure Monitor, is an extensible Application Performance Management (APM) service for developers and DevOps professionals.
Use it to monitor your live applications. It will automatically detect performance anomalies, and includes powerful analytics tools to help you diagnose issues and to understand what users actually do with your app.
References:
https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview 

https://azure.microsoft.com/en-gb/overview/what-is-devops/ 

https://docs.microsoft.com/en-us/azure/advisor/advisor-overview 

https://docs.microsoft.com/en-us/azure/cognitive-services/welcome""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2103
    },
{'q': """Matching""",
        'options': {'Azure SQL Database': 'A managed relational cloud database service', 'Azure SQL Synapse Analytics': 'A cloud-based service that leverages massively parallel processing (MPP) to quickly run complex queries across petabytes of data in a relational database',
                    'Azure Data Lake Analytics': 'Can run massively parallel data transformation and processing programs across petabytes of data', 'Azure HDInsight': 'An Open-source framework for the distributed processing and analysis of big data sets in clusters'},
        'explain_url': 'https://azure.microsoft.com/en-gb/services/data-lake-analytics/',
        'explain': """Box 1: Azure SQL Database -
SQL Server is a relational database service. Azure SQL Database is a managed SQL Server Database in Azure. The SQL Server is managed by Microsoft; you just have access to the database.

Box 2: Azure SQL Synapse Analytics
Azure SQL Synapse Analytics (previously called Data Warehouse) is a cloud-based Platform-as-a-Service (PaaS) offering from Microsoft. It is a large-scale, distributed, MPP (massively parallel processing) relational database technology in the same class of competitors as Amazon Redshift or Snowflake. Azure SQL
Synapse Analytics is an important component of the Modern Data Warehouse multi-platform architecture. Because Azure SQL Synapse Analytics is an MPP system with a shared-nothing architecture across distributions, it is meant for large-scale analytical workloads which can take advantage of parallelism.

Box 3: Azure Data Lake Analytics
You can process big data jobs in seconds with Azure Data Lake Analytics. You can process petabytes of data for diverse workload categories such as querying,
ETL, analytics, machine learning, machine translation, image processing and sentiment analysis by leveraging existing libraries written in .NET languages, R or
Python.

Box 4: Azure HDInsight.
Apache Hadoop was the original open-source framework for distributed processing and analysis of big data sets on clusters. The Hadoop ecosystem includes related software and utilities, including Apache Hive, Apache HBase, Spark, Kafka, and many others.
Azure HDInsight is a fully managed, full-spectrum, open-source analytics service in the cloud for enterprises. The Apache Hadoop cluster type in Azure HDInsight allows you to use HDFS, YARN resource management, and a simple MapReduce programming model to process and analyze batch data in parallel.

Reference:
https://azure.microsoft.com/en-us/services/sql-database/
https://docs.microsoft.com/en-us/azure/sql-data-warehouse/sql-data-warehouse-overview-what-is 
https://docs.microsoft.com/bs-latn-ba/azure/hdinsight/hadoop/apache-hadoop-introduction 
https://www.blue-granite.com/blog/is-azure-sql-data-warehouse-a-good-fit-updated 
https://azure.microsoft.com/en-gb/services/data-lake-analytics/""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2104
    },
{'q': """You need to identify which blades in the Azure portal must be used to perform the following tasks:

✑ View security recommendations.
✑ Monitor the health of Azure services.
✑ Browse available virtual machine images.

Which blade should you identify for each task? To answer, select the appropriate options in the answer area.""",
        'options': {'Monitor the health of Azure services': 'Monitor', 'Browse available virtual machine images': 'Marketplace',
                    'View security recommendations': 'Advisor'},
        'explain_url': '',
        'explain': """Box 1:
Azure Monitor is used to monitor the health of Azure services.
Azure Monitor maximizes the availability and performance of your applications and services by delivering a comprehensive solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments. It helps you understand how your applications are performing and proactively identifies issues affecting them and the resources they depend on.

Box 2:
You can browse available virtual machine images in the Azure Marketplace.
Azure Marketplace provides access and information on solutions and services available from Microsoft and their partners. Customers can discover, try, or buy cloud software solutions built on or for Azure. The catalog of 8,000+ listings provides Azure building blocks, such as Virtual Machines (VMs), APIs, Azure apps,
Solution Templates and managed applications, SaaS apps, containers, and consulting services.

Box 3.
Azure Advisor displays security recommendations.
Azure Advisor provides you with a consistent, consolidated view of recommendations for all your Azure resources. It integrates with Azure Security Center to bring you security recommendations. You can get security recommendations from the Security tab on the Advisor dashboard.
Security Center helps you prevent, detect, and respond to threats with increased visibility into and control over the security of your Azure resources. It periodically analyzes the security state of your Azure resources. When Security Center identifies potential security vulnerabilities, it creates recommendations. The recommendations guide you through the process of configuring the controls you need.

References:
https://docs.microsoft.com/en-us/azure/azure-monitor/overview 
https://docs.microsoft.com/en-us/azure/marketplace/marketplace-faq-publisher-guide 
https://docs.microsoft.com/en-us/azure/advisor/advisor-security-recommendations""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2105
    },
{'q': """After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system.

Solution: You use Bash in Azure Cloud Shell.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cloud-shell/quickstart',
        'explain': """Explanation:
With Azure Cloud Shell, you can create virtual machines using Bash or PowerShell.

Azure Cloud Shell is an interactive, authenticated, browser-accessible shell for managing Azure resources. It provides the flexibility of choosing the shell experience that best suits the way you work, either Bash or PowerShell. 

https://docs.microsoft.com/en-us/azure/cloud-shell/overview""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2106
    },
{'q': """You have an on-premises application that sends email notifications automatically based on a rule.

✑ You plan to migrate the application to Azure.
✑ You need to recommend a serverless computing solution for the application.

What should you include in the recommendation?""",
        'options': {'a web app': None, 'a server image in Azure Marketplace': True, 'a logic app': None, 'an API app': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-overview',
        'explain': """Azure Logic Apps is a cloud service that helps you schedule, automate, and orchestrate tasks, business processes, and workflows when you need to integrate apps, data, systems, and services across enterprises or organizations. Logic Apps simplifies how you design and build scalable solutions for app integration, data integration, system integration, enterprise application integration (EAI), and business-to-business (B2B) communication, whether in the cloud, on premises, or both.

For example, here are just a few workloads you can automate with logic apps:

✑ Process and route orders across on-premises systems and cloud services.

✑ Send email notifications with Office 365 when events happen in various systems, apps, and services.

✑ Move uploaded files from an SFTP or FTP server to Azure Storage.

✑ Monitor tweets for a specific subject, analyze the sentiment, and create alerts or tasks for items that need review.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2107
    },
{'q': """You plan to deploy a website to Azure. The website will be accessed by users worldwide and will host large video files.
You need to recommend which Azure feature must be used to provide the best video playback experience.
What should you recommend?""",
        'options': {'an application gateway': None, 'an Azure ExpressRoute circuit': None, 'a content delivery network (CDN)': True, 'a Azure Traffic Manager profile': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cdn/cdn-overview',
        'explain': """The question states that users are located worldwide and will be downloading large video files. The video playback experience would be improved if they can download the video from servers in the same region as the users. We can achieve this by using a content deliver network.

A content delivery network (CDN) is a distributed network of servers that can efficiently deliver web content to users. CDNs store cached content on edge servers in point-of-presence (POP) locations that are close to end users, to minimize latency.

Azure Content Delivery Network (CDN) offers developers a global solution for rapidly delivering high-bandwidth content to users by caching their content at strategically placed physical nodes across the world. Azure CDN can also accelerate dynamic content, which cannot be cached, by leveraging various network optimizations using CDN POPs. For example, route optimization to bypass Border Gateway Protocol (BGP).

The benefits of using Azure CDN to deliver web site assets include:

✑ Better performance and improved user experience for end users, especially when using applications in which multiple round-trips are required to load content.

✑ Large scaling to better handle instantaneous high loads, such as the start of a product launch event.

✑ Distribution of user requests and serving of content directly from edge servers so that less traffic is sent to the origin server.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2108
    },
    {'q': """Your company plans to deploy several million sensors that will upload data to Azure.
You need to identify which Azure resources must be created to support the planned solution.
Which two Azure resources should you identify? Each correct answer presents part of the solution.""",
        'options': {'Azure Data Lake': True, 'Azure Queue storage': True, 'Azure File Storage': None, 'Azure IoT Hub': True, 'Azure Notification Hubs': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/iot-hub/about-iot-hub',
        'explain': """IoT Hub (Internet of things Hub) provides data from millions of sensors.

IoT Hub is a managed service, hosted in the cloud, that acts as a central message hub for bi-directional communication between your IoT application and the devices it manages. You can use Azure IoT Hub to build IoT solutions with reliable and secure communications between millions of IoT devices and a cloud- hosted solution backend. You can connect virtually any device to IoT Hub.

There are two storage services IoT Hub can route messages to -- Azure Blob Storage and Azure Data Lake Storage Gen2 (ADLS Gen2) accounts. Azure Data

Lake Storage accounts are hierarchical namespace-enabled storage accounts built on top of blob storage. Both of these use blobs for their storage.

References:
https://docs.microsoft.com/en-us/azure/iot-hub/about-iot-hub

https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-messages-d2c""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2109
    },
    {'q': """You have an Azure web app.
You need to manage the settings of the web app from an iPhone.

What are two Azure management tools that you can use? Each correct answer presents a complete solution.""",
        'options': {'Azure CLI': None, 'the Azure portal': True, 'Azure Cloud Shell': True, 'Windows PowerShell': None, 'Azure Storage Explorer': None},
        'explain_url': 'http://www.deployazure.com/management/managing-azure-from-ipad/',
        'explain': """The Azure portal is the web-based portal for managing Azure. Being web-based, you can use the Azure portal on an iPhone.

Azure Cloud Shell is a web-based command line for managing Azure. You access the Azure Cloud Shell from the Azure portal. Being web-based, you can use the

Azure Cloud Shell on an iPhone.

Incorrect Answers:
A: Azure CLI can be installed on MacOS but it cannot be installed on an iPhone.

D: Windows PowerShell can be installed on MacOS but it cannot be installed on an iPhone.

E: Azure Storage Explorer is not used to manage Azure web apps.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2110
    },
{'q': """Your company plans to deploy an Artificial Intelligence (AI) solution in Azure.
What should the company use to build, test, and deploy predictive analytics solutions?""",
        'options': {'Azure Logic Apps': None, 'Azure Machine Learning Designer': True, 'Azure Batch': None, 'Azure Cosmos DB': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer',
        'explain': """Azure Machine Learning designer lets you visually connect datasets and modules on an interactive canvas to create machine learning models.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2111
    },
{'q': """Select all True statements""",
        'options': {'Azure Advisor can generate a list of Azure virtual machines that are protected by Azure Backup': None, 'If you implement the security recommendations provided by Azure Advisor, your companys secure score will decrease': None, 'To maintain Microsoft support, you must implement the security recommendations provided by Azure Advisor within a 30 day period.': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/blog/advisor-backup-recommendations/ ',
        'explain': """Box 1: No -
Azure Advisor does not generate a list of virtual machines that ARE protected by Azure Backup. Azure Advisor does however, generate a list of virtual that ARE NOT protected by Azure Backup. You can view a list of virtual machines that are protected by Azure Backup by viewing the Protected Items in the Azure Recovery Services Vault.

Box 2: No -
If you implement the security recommendations, you company's score will increase, not decrease.

Box 3: No -
There is no requirement to implement the security recommendations provided by Azure Advisor. The recommendations are just that, recommendationsג. They are not requirements.

References:
https://azure.microsoft.com/en-gb/blog/advisor-backup-recommendations/ 

https://docs.microsoft.com/en-us/azure/advisor/advisor-overview 

https://microsoft.github.io/AzureTipsAndTricks/blog/tip173.html""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2112
    },
{'q': """What can you use to automatically send an alert if an administrator stops an Azure virtual machine?""",
        'options': {'Azure Advisor': None, 'Azure Service Health': None, 'Azure Monitor': True, 'Azure Network Watcher': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-monitor/insights/vminsights-alerts',
        'explain': """https://docs.microsoft.com/en-us/azure/azure-monitor/insights/vminsights-alerts""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2113
    },
{'q': """Matching""",
        'options': {'Azure Machine Learning': 'Uses past trainings to provide predictions that have high probability', 'Azure Synapse Analytics': 'Provides a cloud-based Enterprise Data Warehouse',
                    'Azure Functions': 'Provides serverless computing functionalities', 'Azure IoT Hub': 'Process data from millions of sensors'},
        'explain_url': 'https://azure.microsoft.com/en-gb/services/synapse-analytics/',
        'explain': """Box 1: Azure SQL Synapse Analytics
Azure SQL Synapse Analytics (previously called Data Warehouse) is a cloud-based Platform-as-a-Service (PaaS) offering from Microsoft. It is a large-scale, distributed, MPP (massively parallel processing) relational database technology in the same class of competitors as Amazon Redshift or Snowflake. Azure SQL
Synapse Analytics is an important component of the Modern Data Warehouse multi-platform architecture. Because Azure SQL Synapse Analytics is an MPP system with a shared-nothing architecture across distributions, it is meant for large-scale analytical workloads which can take advantage of parallelism.

Box 2:
Azure Machine Learning uses past trainings to provide predictions that have high probability.
Machine learning is a data science technique that allows computers to use existing data to forecast future behaviors, outcomes, and trends. By using machine learning, computers learn without being explicitly programmed.
Forecasts or predictions from machine learning can make apps and devices smarter. For example, when you shop online, machine learning helps recommend other products you might want based on what you've bought.

Box 3:
Azure Functions provides serverless computing functionalities.
Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure.

Box 4:
IoT Hub (Internet of things Hub) provides data from millions of sensors.
IoT Hub is a managed service, hosted in the cloud, that acts as a central message hub for bi-directional communication between your IoT application and the devices it manages. You can use Azure IoT Hub to build IoT solutions with reliable and secure communications between millions of IoT devices and a cloud- hosted solution backend. You can connect virtually any device to IoT Hub.

Reference:
https://azure.microsoft.com/en-gb/services/synapse-analytics/ 
https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-ml 
https://docs.microsoft.com/en-us/azure/iot-hub/about-iot-hub 
https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2114
    },
{'q': """You need to create a new Azure virtual machine from a tablet that runs the Android operating system.
What are three possible solutions? Each correct answer presents a complete solution.""",
        'options': {'Use Bash in Azure Cloud Shell.': True, 'Use PowerShell in Azure Cloud Shell.': True, ' Use the PowerApps portal.': None, 'Use the Security & Compliance admin center.': None, 'Use the Azure portal.': True},
        'explain_url': '',
        'explain': """The Android tablet device will have a web browser (Chrome). Thats enough to connect to the Azure portal.
The Azure portal offers three ways to create a VM:
✑ Using the graphical portal.
✑ Using the Azure Cloud Shell using Bash.
✑ Using the Azure Cloud Shell using PowerShell.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2115
    },
{'q': """A team of developers at your company plans to deploy, and then remove, 50 virtual machines each week. All the virtual machines are configured by using Azure
Resource Manager templates.
You need to recommend which Azure service will minimize the administrative effort required to deploy and remove the virtual machines.
What should you recommend?""",
        'options': {'Azure Reserved Virtual Machine (VM) Instances': None, 'Azure DevTest Labs': True, 'Azure virtual machine scale sets': None, 'Microsoft Managed Desktop': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/lab-services/devtest-lab-overview',
        'explain': """DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates.

By using DevTest Labs, you can test the latest versions of your applications by doing the following tasks:
✑ Quickly provision Windows and Linux environments by using reusable templates and artifacts.
✑ Easily integrate your deployment pipeline with DevTest Labs to provision on-demand environments.
✑ Scale up your load testing by provisioning multiple test agents and create pre-provisioned environments for training and demos""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2116
    },
{'q': """Select all True statements""",
        'options': {'Azure Advisor provides recommendations on how to improve security of an Azure Active Directory environment': None, 'Azure Advisor provides recommendations on how to reduce the cost of running Azure virtual machines': True,
                    'Azure Advisor provides recommendations on how to configure the network settings on Azure virtual machines': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/advisor/advisor-security-recommendations',
        'explain': """Box 1: No -
Azure Advisor provides you with a consistent, consolidated view of recommendations for all your Azure resources. It integrates with Azure Security Center to bring you security recommendations. You can get security recommendations from the Security tab on the Advisor dashboard. Examples of recommendations include restricting access to virtual machines by configuring Network Security Groups, enabling storage encryption, installing vulnerability assessment solutions.

However, Azure Advisor does not provide recommendations on how to improve the security of an Azure AD environment.

Box 2: Yes
Advisor helps you optimize and reduce your overall Azure spend by identifying idle and underutilized resources. You can get cost recommendations from the Cost tab on the Advisor dashboard.

Box 3: No.
Azure Advisor does not provide recommendations on how to configure network settings on Azure virtual machines.
References:
https://docs.microsoft.com/en-us/azure/advisor/advisor-security-recommendations https://docs.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'multi',
        'id': 2117
    },
{'q': """You have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1.
From Azure documentation, you have the following command that creates a virtual machine named VM1. az vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys
You need to create VM1 in Subscription1 by using the command.

Solution: From the Azure portal, launch Azure Cloud Shell and select PowerShell. Run the command in Cloud Shell.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli',
        'explain': """The command can be run in the Azure Cloud Shell. Although this question says you select PowerShell rather than Bash, the Az commands will work in
PowerShell.
The Azure Cloud Shell is a free interactive shell. It has common Azure tools preinstalled and configured to use with your account.

To open the Cloud Shell, just select Try it from the upper right corner of a code block. You can also launch Cloud Shell in a separate browser tab by going to https://shell.azure.com/bash.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2118
    },
{'q': """You have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1.
From Azure documentation, you have the following command that creates a virtual machine named VM1. 
az vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys
You need to create VM1 in Subscription1 by using the command.

Solution: From a computer that runs Windows 10, install Azure CLI. From PowerShell, sign in to Azure and then run the command.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest',
        'explain': """The command can be run from PowerShell or the command prompt if you have the Azure CLI installed. However, it must be run on the Windows 10 computer, not in Azure.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2119
    },
{'q': """You have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1.
From Azure documentation, you have the following command that creates a virtual machine named VM1. 
az vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys

You need to create VM1 in Subscription1 by using the command.

Solution: From a computer that runs Windows 10, install Azure CLI. From a command prompt, sign in to Azure and then run the command.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest',
        'explain': """The command can be run from PowerShell or the command prompt if you have the Azure CLI installed. However, it must be run on the Windows 10 computer, not in Azure.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2120
    },
{'q': """Several support engineers plan to manage Azure by using the computers shown in the following table: 
✑ COMPUTER1: Windows10, 
✑ COMPUTER2: Ubuntu, 
✑ COMPUTER3: MACOS.  

You need to identify which Azure management tools can be used from each computer.""",
        'options': {'The Azure CLI': None, 'Azure Portal': None, 'Azure Powershell': None, 'Azure CLI and Azure Powershell': None, 'Azure CLI, Azure Powershell and Azure Portal': True},
        'explain_url': 'https://buildazure.com/2016/08/18/powershell-now-open-source-and-cross-platform-linux-macos-windows/',
        'explain': """Previously, the Azure CLI (or x-plat CLI) was the only option for managing Azure subscriptions and resources from the command-line on Linux and macOS. Now with the open source and cross-platform release of PowerShell, you'll be able to manage all your Azure resources from Windows, Linux and macOS using your tool of choice, either the Azure CLI or Azure PowerShell cmdlets.

The Azure portal runs in a web browser so can be used in either operating system.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2121
    },
{'q': """Fill in the blank.  You can access Compliance Manager from the _________""",
        'options': {'Azure Active Directory admin center': None, 'Azure Portal': True, 'Microsoft 365 admin center': None, 'Microsoft Service Trust Portal': None},
        'explain_url': '',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2122
    },
{'q': """Fill in the blank.  _________  common platform for deploying objects to a cloud infrastructure and for implementing consistency across the Azure environment""",
        'options': {'Azure policies provide': None, 'Resource groups provide': True, 'Azure Resource Manager templates provide': True, 'Management groups provide': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/policy/overview',
        'explain': """Azure Resource Manager templates provides a common platform for deploying objects to a cloud infrastructure and for implementing consistency across the Azure environment.

Azure policies are used to define rules for what can be deployed and how it should be deployed. Whilst this can help in ensuring consistency, Azure policies do not provide the common platform for deploying objects to a cloud infrastructure.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2123
    },
{'q': """Matching""",
        'options': {'Azure Bot Services': 'Provides a digital online assistant that provides speech support', 'Azure Machine Learning': 'Uses past trainings to provide predictions that have a high probability',
                    'Azure Functions': 'Provides serverless computing functionality', 'Azure IoT Hub': 'Processes data from millions of sensors'},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0',
        'explain': """Azure Bot Services provides a digital online assistant that provides speech support.
Bots provide an experience that feels less like using a computer and more like dealing with a person - or at least an intelligent robot. They can be used to shift simple, repetitive tasks, such as taking a dinner reservation or gathering profile information, on to automated systems that may no longer require direct human intervention. Users converse with a bot using text, interactive cards, and speech. A bot interaction can be a quick question and answer, or it can be a sophisticated conversation that intelligently provides access to services.

Box 2:
Azure Machine Learning uses past trainings to provide predictions that have high probability.
Machine learning is a data science technique that allows computers to use existing data to forecast future behaviors, outcomes, and trends. By using machine learning, computers learn without being explicitly programmed.
Forecasts or predictions from machine learning can make apps and devices smarter. For example, when you shop online, machine learning helps recommend other products you might want based on what you've bought.

Box 3:
Azure Functions provides serverless computing functionalities.
Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure.

Box 4:
IoT Hub (Internet of things Hub) provides data from millions of sensors.
IoT Hub is a managed service, hosted in the cloud, that acts as a central message hub for bi-directional communication between your IoT application and the devices it manages. You can use Azure IoT Hub to build IoT solutions with reliable and secure communications between millions of IoT devices and a cloud- hosted solution backend. You can connect virtually any device to IoT Hub.

References:
https://docs.microsoft.com/en-us/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0 
https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-ml 
https://docs.microsoft.com/en-us/azure/azure-functions/ 
https://docs.microsoft.com/en-us/azure/iot-hub/about-iot-hub""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2124
    },
{'q': """An Azure administrator plans to run a PowerShell script that creates Azure resources.
You need to recommend which computer configuration to use to run the script.
Solution: Run the script from a computer that runs Windows 10 and has the Azure PowerShell module installed.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/powershell/scripting/components/ise/how-to-write-and-run-scripts-in-the-windows-powershell-ise?view=powershell-6',
        'explain': """A PowerShell script is a file that contains PowerShell cmdlets and code. A PowerShell script needs to be run in PowerShell.

In this question, the computer has the Azure PowerShell module installed. Therefore, this solution does meet the goal.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2125
    },
{'q': """""",
        'options': {'Azure Virtual Machines': 'Provide operating system virtualization', 'Azure Container Instances': 'Provide portable environment for virtualized application',
                    'Azure App Service': 'Used to build, deploy, and scale web apps', 'Azure Functions': 'Provide platform for serverless code'},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-machines/windows/overview',
        'explain': """Box 1:
Azure virtual machines provide operation system virtualization.
Azure Virtual Machines (VM) is one of several types of on-demand, scalable computing resources that Azure offers. Typically, you choose a VM when you need more control over the computing environment than the other choices offer.

Box 2:
Azure Container Instances provide portable environments for virtualized applications.
Containers are becoming the preferred way to package, deploy, and manage cloud applications. Azure Container Instances offers the fastest and simplest way to run a container in Azure, without having to manage any virtual machines and without having to adopt a higher-level service.
Containers offer significant startup benefits over virtual machines (VMs). Azure Container Instances can start containers in Azure in seconds, without the need to provision and manage VMs.

Box 3:
Azure App Service is used to build, deploy and scale web apps.
Azure App Service is a platform-as-a-service (PaaS) offering that lets you create web and mobile apps for any platform or device and connect to data anywhere, in the cloud or on-premises. App Service includes the web and mobile capabilities that were previously delivered separately as Azure Websites and Azure Mobile
Services.

Box 4:
Azure Functions provide a platform for serverless code.
Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure.

References:
https://docs.microsoft.com/en-us/azure/virtual-machines/windows/overview 
https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-app-services 
https://docs.microsoft.com/en-us/azure/azure-functions/ 
https://docs.microsoft.com/en-us/azure/container-instances/container-instances-overview""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'match',
        'id': 2126
    },
{'q': """Which service provides serverless computing in Azure?""",
        'options': {'Azure Virtual Machines': None, 'Azure Functions': True, 'Azure storage account': None, 'Azure dedicated hosts': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-functions/',
        'explain': """Azure Functions provide a platform for serverless code.

Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2127
    },
{'q': """An Azure administrator plans to run a PowerShell script that creates Azure resources.
You need to recommend which computer configuration to use to run the script.

Which three computers can run the script? Each correct answer presents a complete solution.""",
        'options': {'a computer that runs macOS and has PowerShell Core 6.0 installed.': True, 'a computer that runs Windows 10 and has the Azure PowerShell module installed.': True,
                    'a computer that runs Linux and has the Azure PowerShell module installed.': None, 'a computer that runs Linux and has the Azure CLI tools installed.': None, 'a computer that runs Chrome OS and uses Azure Cloud Shell.': True},
        'explain_url': 'https://docs.microsoft.com/en-us/powershell/scripting/components/ise/how-to-write-and-run-scripts-in-the-windows-powershell-ise?view=powershell-6 https://docs.microsoft.com/en-us/azure/cloud-shell/quickstart-powershell',
        'explain': """A PowerShell script is a file that contains PowerShell cmdlets and code. A PowerShell script needs to be run in PowerShell.""",
        'notes': '',
        'history': '',
        'category': 'core',
        'q_type': 'basic',
        'id': 2128
    },
{'q': """Select all True statements""",
        'options': {'Azure Firewall will encrypt all the network traffic sent from Azure to the Internet': None, 'A network security group (NSG) will encrypt all the network traffic sent from Azure to the Internet': None,
                    'Azure virtual machines that run Windows Server 2016 can encrypt network traffic sent to the Internet': None,},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/security/azure-security-data-encryption-best-practices#protect-data-in-transit',
        'explain': """Box 1: No -
Azure firewall does not encrypt network traffic. It is used to block or allow traffic based on source/destination IP address, source/destination ports and protocol.

Box 2: No -
A network security group does not encrypt network traffic. It works in a similar way to a firewall in that it is used to block or allow traffic based on source/ destination IP address, source/destination ports and protocol.

Box 3: No -
The question is rather vague as it would depend on the configuration of the host on the Internet. Windows Server does come with a VPN client and it also supports other encryption methods such IPSec encryption or SSL/TLS so it could encrypt the traffic if the Internet host was configured to require or accept the encryption.
However, the VM could not encrypt the traffic to an Internet host that is not configured to require the encryption.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'multi',
        'id': 2129
    },
{'q': """Select all True statements""",
        'options': {'Azure Security Center can monitor Azure resources and on-premises resources': True, 'All Azure Security Center features are free': None, 'Fro Azure Security Center, you can download a Regulatory Compliance Report': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/security-center/security-center-intro',
        'explain': """Box 1: Yes -
Azure Security Center is a unified infrastructure security management system that strengthens the security posture of your data centers, and provides advanced threat protection across your hybrid workloads in the cloud - whether they're in Azure or not - as well as on premises.

Box 2: No -
Only two features: Continuous assessment and security recommendations, and Azure secure score, are free.

Box 3: Yes -
The advanced monitoring capabilities in Security Center also let you track and manage compliance and governance over time. The overall compliance provides you with a measure of how much your subscriptions are compliant with policies associated with your workload.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'multi',
        'id': 2130
    },
{'q': """You need to configure an Azure solution that meets the following requirements:
1) Secures websites from attacks 2) Generates reports that contain details of attempted attacks
What should you include in the solution?""",
        'options': {'Azure Firewall': None, 'a network security group (NSG)': None, 'Azure Information Protection': None, 'DDoS protection': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/security/fundamentals/ddos-best-practices',
        'explain': """DDoS is a type of attack that tries to exhaust application resources. The goal is to affect the applicationג€™s availability and its ability to handle legitimate requests.

DDoS attacks can be targeted at any endpoint that is publicly reachable through the internet.

Azure has two DDoS service offerings that provide protection from network attacks: DDoS Protection Basic and DDoS Protection Standard.

DDoS Basic protection is integrated into the Azure platform by default and at no extra cost.

You have the option of paying for DDoS Standard. It has several advantages over the basic service, including logging, alerting, and telemetry. DDoS Standard can generate reports that contain details of attempted attacks as required in this question.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2131
    },
{'q': """Matching""",
        'options': {'Monitor threats by using sensors': 'Azure Advanced Threat Protection (ATP)', 'Enforce Azure MFA based condition': 'Azure Active Directory Identity Protection'},
        'explain_url': 'https://docs.microsoft.com/en-us/azure-advanced-threat-protection/what-is-atp https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-mfa-policy',
        'explain': """Box 1:
To monitor threats by using sensors, you would use Azure Advanced Threat Protection (ATP).
Azure Advanced Threat Protection (ATP) is a cloud-based security solution that leverages your on-premises Active Directory signals to identify, detect, and investigate advanced threats, compromised identities, and malicious insider actions directed at your organization.
Sensors are software packages you install on your servers to upload information to Azure ATP.

Box 2:
To enforce MFA based on a condition, you would use Azure Active Directory Identity Protection.
Azure AD Identity Protection helps you manage the roll-out of Azure Multi-Factor Authentication (MFA) registration by configuring a Conditional Access policy to require MFA registration no matter what modern authentication app you are signing in to.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'match',
        'id': 2132
    },
{'q': """Your Azure environment contains multiple Azure virtual machines.
You need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP.
What are two possible solutions? Each correct answer presents a complete solution.""",
        'options': {'Modify an Azure Traffic Manager profile': None, 'Modify a network security group (NSG)': True, 'Modify a DDoS protection plan': None, 'Modify an Azure firewall': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/security-overview',
        'explain': """https://docs.microsoft.com/en-us/azure/virtual-network/security-overview""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2133
    },
{'q': """Fill in the blank.  You can enable just in time (JIT)) VM access by using __________""",
        'options': {'Azure Bastion': None, 'Azure Firewall': None, 'Azure Front Door': None, 'Azure Security Center': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc',
        'explain': """The just-in-time (JIT) virtual machine (VM) access feature in Azure Security Center allows you to lock down inbound traffic to your Azure Virtual Machines. This reduces exposure to attacks while providing easy access when you need to connect to a VM.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2134
    },
{'q': """Select all True statements""",
        'options': {'You can associate a network security group (NSG) to a virtual network subnet': True, 'You can associate a network security group (NSG) to a virtual network': None, 'You can associate a network security group (NSG) to a network interface': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/network-security-group-how-it-works',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'multi',
        'id': 2135
    },
{'q': """You have an Azure environment that contains 10 virtual networks and 100 virtual machines.
You need to limit the amount of inbound traffic to all the Azure virtual networks.
What should you create?""",
        'options': {'one application security group (ASG)': None, '10 virtual network gateways': None, '10 Azure ExpressRoute circuits': None, 'one Azure firewall': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/firewall/overview',
        'explain': """You can restrict traffic to multiple virtual networks with a single Azure firewall.

Azure Firewall is a managed, cloud-based network security service that protects your Azure Virtual Network resources. It's a fully stateful firewall as a service with built-in high availability and unrestricted cloud scalability.

You can centrally create, enforce, and log application and network connectivity policies across subscriptions and virtual networks. Azure Firewall uses a static public IP address for your virtual network resources allowing outside firewalls to identify traffic originating from your virtual network.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2136
    },
{'q': """Azure Key Vault is used to store secrets for Azure Active Directory (Azure AD) user accounts.""",
        'options': {'No change is needed': None, 'Azure Active Directory (Azure AD) administrative accounts': None,
                    'Personally Identifiable Information (PII)': None, 'server applications': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/key-vault/key-vault-overview https://docs.microsoft.com/en-us/learn/modules/manage-secrets-with-azure-key-vault/',
        'explain': """Centralizing storage of application secrets in Azure Key Vault allows you to control their distribution. Key Vault greatly reduces the chances that secrets may be accidentally leaked. When using Key Vault, application developers no longer need to store security information in their application. Not having to store security information in applications eliminates the need to make this information part of the code. For example, an application may need to connect to a database. Instead of storing the connection string in the app's code, you can store it securely in Key Vault.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2137
    },
{'q': """Your company plans to automate the deployment of servers to Azure.
Your manager is concerned that you may expose administrative credentials during the deployment.
You need to recommend an Azure solution that encrypts the administrative credentials during the deployment.

What should you include in the recommendation?""",
        'options': {'Azure Key Vault': None, 'Azure Information Protection': True,
                    'Azure Security Center': None, 'Azure Multi-Factor Authentication (MFA)': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/key-vault/key-vault-overview',
        'explain': """Azure Key Vault is a secure store for storage various types of sensitive information. In this question, we would store the administrative credentials in the Key Vault.

With this solution, there is no need to store the administrative credentials as plain text in the deployment scripts.
All information stored in the Key Vault is encrypted.
A
zure Key Vault can be used to Securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets.

Secrets and keys are safeguarded by Azure, using industry-standard algorithms, key lengths, and hardware security modules (HSMs). The HSMs used are

Federal Information Processing Standards (FIPS) 140-2 Level 2 validated.

Access to a key vault requires proper authentication and authorization before a caller (user or application) can get access. Authentication establishes the identity of the caller, while authorization determines the operations that they are allowed to perform.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2138
    },
{'q': """You plan to deploy several Azure virtual machines.
You need to control the ports that devices on the Internet can use to access the virtual machines.
What should you use?""",
        'options': {'a network security group (NSG)': True, 'an Azure Active Directory (Azure AD) role': None,
                    'an Azure Active Directory group': None, 'an Azure key vault': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/security-overview',
        'explain': """https://docs.microsoft.com/en-us/azure/virtual-network/security-overview""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2139
    },
{'q': """Fill in the blank.  After you create a virtual machine, you can modify the ____________ to allow connections to TCP port 8080 on a virtual machine""",
        'options': {'network security group (NSG)': True, 'virtual network gateway': None,
                    'virtual network': None, 'route table': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/security-overview',
        'explain': """When you create a virtual machine, the default setting is to create a Network Security Group attached to the network interface assigned to a virtual machine.

A network security group works like a firewall. You can attach a network security group to a virtual network and/or individual subnets within the virtual network.

You can also attach a network security group to a network interface assigned to a virtual machine. You can use multiple network security groups within a virtual network to restrict traffic between resources such as virtual machines and subnets.

You can filter network traffic to and from Azure resources in an Azure virtual network with a network security group. A network security group contains security rules that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources.

In this question, we need to add a rule to the network security group to allow the connection to the virtual machine on port 8080.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2140
    },
{'q': """Select all True statements""",
        'options': {'You can create custom Azure roles to control access to resources': True, 'A user account can be assigned to multiple Azure roles': True,
                    'A resource group can have the Owner role assigned to multiple users': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'multi',
        'id': 2141
    },
{'q': """Your Azure environment contains multiple Azure virtual machines.
You need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP.

Solution: You modify a network security group (NSG).
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/security-overview',
        'explain': """A network security group works like a firewall. You can attach a network security group to a virtual network and/or individual subnets within the virtual network.

You can also attach a network security group to a network interface assigned to a virtual machine. You can use multiple network security groups within a virtual network to restrict traffic between resources such as virtual machines and subnets.

You can filter network traffic to and from Azure resources in an Azure virtual network with a network security group. A network security group contains security rules that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources.

In this question, we need to add a rule to the network security group to allow the connection to the virtual machine on port 80 (HTTP).""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2142
    },
{'q': """Your Azure environment contains multiple Azure virtual machines.
You need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP.

Solution: You modify a DDoS protection plan.
Does this meet the goal?""",
'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview',
        'explain': """DDoS is a form of attack on a network resource. A DDoS protection plan is used to protect against DDoS attacks; it does not provide connectivity to a virtual machine.
To ensure that a virtual machine named VM1 is accessible from the Internet over HTTP, you need to modify a network security group or Azure Firewall.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2143
    },
{'q': """You need to collect and automatically analyze security events from Azure Active Directory (Azure AD).
What should you use?""",
        'options': {'Azure Sentinel': True, 'Azure Synapse Analytics': None,
                    'Azure AD Connect': None, 'Azure Key Vault': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/sentinel/overview',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2144
    },
{'q': """Your Azure environment contains multiple Azure virtual machines.
You need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP.
Solution: You modify an Azure firewall.
Does this meet the goal?""",
'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/firewall/overview',
        'explain': """Azure Firewall is a managed, cloud-based network security service that protects your Azure Virtual Network resources. It's a fully stateful firewall as a service with built-in high availability and unrestricted cloud scalability.

In this question, we need to add a rule to Azure Firewall to allow the connection to the virtual machine on port 80 (HTTP).""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2145
    },
{'q': """Your Azure environment contains multiple Azure virtual machines.
You need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP.

Solution: You modify an Azure Traffic Manager profile.
Does this meet the goal?""",
'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/traffic-manager/traffic-manager-overview',
        'explain': """Azure Traffic Manager is a DNS-based load balancing solution. It is not used to ensure that a virtual machine named VM1 is accessible from the Internet over
HTTP.
To ensure that a virtual machine named VM1 is accessible from the Internet over HTTP, you need to modify a network security group or Azure Firewall.

In this question, we need to add a rule to a network security group or Azure Firewall to allow the connection to the virtual machine on port 80 (HTTP).""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2146
    },
{'q': """Your company plans to deploy several web servers and several database servers to Azure.
You need to recommend an Azure solution to limit the types of connections from the web servers to the database servers.

What should you include in the recommendation?""",
        'options': {'network security groups (NSGs)': None, 'Azure Service Bus': True,
                    'a local network gateway': None, 'a route filter': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/virtual-network/security-overview',
        'explain': """A network security group works like a firewall. You can attach a network security group to a virtual network and/or individual subnets within the virtual network.

You can also attach a network security group to a network interface assigned to a virtual machine. You can use multiple network security groups within a virtual network to restrict traffic between resources such as virtual machines and subnets.

You can filter network traffic to and from Azure resources in an Azure virtual network with a network security group. A network security group contains security rules that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2147
    },
{'q': """Fill in the blank.  From _________ you can view which user turned off a specific virtual machine during the last 14 days.""",
        'options': {'Azure Access Control IAM': None, 'Azure  Event Hubs': None,
                    'Azure Activity Log': True, 'Azure Service Health': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-audit',
        'explain': """You would use the Azure Activity Log, not Access Control to view which user turned off a specific virtual machine during the last 14 days.

Activity logs are kept for 90 days. You can query for any range of dates, as long as the starting date isn't more than 90 days in the past.

In this question, we would create a filter to display shutdown operations on the virtual machine in the last 14 days.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2148
    },
{'q': """Which service provides network traffic filtering across multiple Azure subscriptions and virtual networks?""",
        'options': {'Azure Firewall': True, 'an application security group': None,
                    'Azure DDoS protection': None, 'a network security group (NSG)': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/firewall/overview',
        'explain': """https://docs.microsoft.com/en-us/azure/firewall/overview""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2149
    },
{'q': """Which Azure service should you use to store certificates?""",
        'options': {'Azure Security Center': None, 'an Azure Storage account': None,
                    'Azure Key Vault': True, 'Azure Information Protection': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/key-vault/key-vault-overview',
        'explain': """Azure Key Vault is a secure store for storage various types of sensitive information including passwords and certificates.

Azure Key Vault can be used to Securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets.

Secrets and keys are safeguarded by Azure, using industry-standard algorithms, key lengths, and hardware security modules (HSMs). The HSMs used are

Federal Information Processing Standards (FIPS) 140-2 Level 2 validated.

Access to a key vault requires proper authentication and authorization before a caller (user or application) can get access. Authentication establishes the identity of the caller, while authorization determines the operations that they are allowed to perform.""",
        'notes': '',
        'history': '',
        'category': 'security',
        'q_type': 'basic',
        'id': 2150
    },
{
    'q': 'Which Azure service can you use as a security information and event management (SIEM) solution?',
    'options': {'Azure Analysis Services': None, 'Azure Cognitive Services': None,
                'Azure Sentinel': True, 'Azure Information Protection': None},
    'explain_url': 'https://azure.microsoft.com/en-in/services/azure-sentinel/',
    'explain': '',
    'notes': '',
    'history': '',
    'category': '',
    'q_type': 'basic',
    'id': 2151
    },
{'q': """What can Azure Information Protection encrypt?""",
        'options': {'network traffic': None, 'documents and email messages': True,
                    'an Azure Storage account': None, 'an Azure SQL database': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection ',
        'explain': """Azure Information Protection can encrypt documents and emails.

Azure Information Protection is a cloud-based solution that helps an organization to classify and optionally, protect its documents and emails by applying labels.

Labels can be applied automatically by administrators who define rules and conditions, manually by users, or a combination where users are given recommendations.

The protection technology uses Azure Rights Management (often abbreviated to Azure RMS). This technology is integrated with other Microsoft cloud services and applications, such as Office 365 and Azure Active Directory.

This protection technology uses encryption, identity, and authorization policies. Similarly to the labels that are applied, protection that is applied by using Rights

Management stays with the documents and emails, independently of the location inside or outside your organization, networks, file servers, and applications.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2152
    },
{'q': """What should you use to evaluate whether your companys Azure environment meets regulatory requirements?""",
        'options': {'the Knowledge Center website': None, 'the Advisor blade from the Azure portal': True,
                    'Compliance Manager from the Service Trust Portal': None, 'the Solutions blade from the Azure portal': None},
        'explain_url': 'https://docs.microsoft.com/en-us/microsoft-365/compliance/get-started-with-service-trust-portal?view=o365-worldwide',
        'explain': """Compliance Manager in the Service Trust Portal is a workflow-based risk assessment tool that helps you track, assign, and verify your organization's regulatory compliance activities related to Microsoft Cloud services, such as Microsoft 365, Dynamics 365, and Azure.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2153
    },
{'q': """Fill in the blank. Your company implements ____________ automatically add a watermark to Microsoft Word documents that contain credit card information.""",
        'options': {'Azure policies': None, 'DDoS protection': None,
                    'Azure Information Protection': True, 'Azure Active Directory Identity Protection': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection',
        'explain': """Azure Information Protection is used to automatically add a watermark to Microsoft Word documents that contain credit card information.

You use Azure Information Protection labels to apply classification to documents and emails. When you do this, the classification is identifiable regardless of where the data is stored or with whom itג€™s shared. The labels can include visual markings such as a header, footer, or watermark.

Labels can be applied automatically by administrators who define rules and conditions, manually by users, or a combination where users are given recommendations. In this question, we would configure a label to be automatically applied to Microsoft Word documents that contain credit card information. The label would then add the watermark to the documents.

Reference:
https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection 
https://docs.microsoft.com/en-us/azure/information-protection/infoprotect-quick-start-tutorial""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2154
    },
{'q': """You have a Azure virtual netowrk named VNET1 in a resource group named RG1.  You assign the Azure Policy definition of Not Allowed Resource Type and specify that virtual networks are not allowed resource type in RG1.  VNET1 ________""",
        'options': {'is deleted automatically': None, 'is moved automatically to another resource group': None,
                    'continues to function normally': True, 'is now a read-only object': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/policy/overview https://docs.microsoft.com/en-us/azure/governance/policy/assign-policy-portal',
        'explain': """The VNet will be marked as Non-compliant when the policy is assigned. However, it will not be deleted and will continue to function normally.

Azure Policy is a service in Azure that you use to create, assign, and manage policies. These policies enforce different rules and effects over your resources, so those resources stay compliant with your corporate standards and service level agreements.

If there are any existing resources that aren't compliant with a new policy assignment, they appear under Non-compliant resources.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2155
    },
{'q': """Your company has an Azure subscription that contains resources in several regions.
A company policy states that administrators must only be allowed to create additional Azure resources in a region in the country where their office is located.

You need to create the Azure resource that must be used to meet the policy requirement.
What should you create?""",
        'options': {'a read-only lock': None, 'an Azure policy': True,
                    'a management group': None, 'a reservation': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/policy/overview',
        'explain': """Azure policies can be used to define requirements for resource properties during deployment and for already existing resources. Azure Policy controls properties such as the types or locations of resources.

Azure Policy is a service in Azure that you use to create, assign, and manage policies. These policies enforce different rules and effects over your resources, so those resources stay compliant with your corporate standards and service level agreements. Azure Policy meets this need by evaluating your resources for non- compliance with assigned policies. All data stored by Azure Policy is encrypted at rest.

Azure Policy offers several built-in policies that are available by default. In this question, we would use the ג€˜Allowed Locationsג€™ policy to define the locations where resources can be deployed.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2156
    },
{'q': """From Azure Cloud Shell, you can track your companys regulatory standards and regulations, such as ISO 27001.""",
        'options': {'No change is needed': None, 'the Microsoft Cloud Partner Portal': None,
                    'Compliance Manager': True, 'the Trust Center': None},
        'explain_url': 'https://docs.microsoft.com/en-us/microsoft-365/compliance/compliance-manager-overview',
        'explain': """Microsoft Compliance Manager (Preview) is a free workflow-based risk assessment tool that lets you track, assign, and verify regulatory compliance activities related to Microsoft cloud services. Azure Cloud Shell, on the other hand, is an interactive, authenticated, browser-accessible shell for managing Azure resources.
References:
https://docs.microsoft.com/en-us/microsoft-365/compliance/compliance-manager-overview 
https://docs.microsoft.com/en-us/azure/cloud-shell/overview""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2157
    },
{'q': """Select all True statements""",
        'options': {'You can create Group Policies in Azure Active Directory': True, 'You can join Windows 10 devices to Azure Active Directory': True,
                    'You can join Android devices to Azure Active Directory': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory-domain-services/manage-group-policy',
        'explain': """Azure AD join only applies to Windows 10 devices.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2158
    },
{'q': """Fill in the blank. The __________ explains what data Microsoft processes, how Microsoft processes the data and the purpose of processing the data.""",
        'options': {'Microsoft Online Services Privacy Satatment': True, 'Microsoft Online Services Terms': None,
                    'Microsoft Online Services Level Agreement': None, 'Online Subscription Agreement for MS Azure': None},
        'explain_url': 'https://privacy.microsoft.com/en-us/privacystatement',
        'explain': """The Microsoft Privacy Statement explains what personal data Microsoft processes, how Microsoft processes the data, and the purpose of processing the data""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2159
    },
{'q': """Fill in the blank.  is the process of verifing a users credentials""",
        'options': {'Authorization': None, 'Authentication': True,
                    'Federation': None, 'Ticketing': None},
        'explain_url': '',
        'explain': """Authentication, not authorization is the process of verifying a users  credentials.

The difference between authentication and authorization is:

Authentication is proving your identity, proving that you are who you say you are. The most common example of this is logging in to a system by providing credentials such as a username and password.

✑ Authorization is what your are allowed to do once you've been authenticated. For example, what resources you are allowed to access and what you can do with those resources.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2160
    },{'q': """Fill in the blank. An Azure Policy initiative definition is a _____________""",
        'options': {'collection of policy definations': True, 'collection of Azure Policy definition assignments': None,
                    'group of Azure Blueprint definitions': None, 'group of role-based access control (RBAC) role assignments': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/policy/overview',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2161
    },
{'q': """"Fill in the blank. ___________ provide organizations with the ability to manage the compliance of Azure resources across multiple subscriptions""",
        'options': {'Resource groups': None, 'Management groups': None,
                    'Azure Policies': True, 'Azure App Service Plans': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/policy/overview',
        'explain': """'https://docs.microsoft.com/en-us/azure/governance/policy/overview""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2162
    },
{'q': """Select all True statements""",
        'options': {'General Data Protection Regulation (GDPR) defines data protection and privacy rules': True, 'General Data Protection Regulation (GDPR) applies to companies that offer goods and services to individuals in the EU': True,
                    'Azure can be used to build a General Data Protection Regulation (GDPR)-compliant infrastructure': True},
        'explain_url': 'https://azure.microsoft.com/en-gb/blog/new-capabilities-to-enable-robust-gdpr-compliance/',
        'explain': """https://azure.microsoft.com/en-gb/blog/new-capabilities-to-enable-robust-gdpr-compliance/""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2163
    },
{'q': """Select all True statements""",
        'options': {'You can add an Azure Resource Manager template to an Azure blueprint': True, 'You can assign an Azure blueprint to a resource group': None,
                    'You can use Azure Blueprints to grant permissions to a resource': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/blueprints/overview',
        'explain': """https://docs.microsoft.com/en-us/azure/governance/blueprints/overview""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2164
    },
{
        'q': 'Select all True statements',
        'options': {'Azure China is operated by Microsoft': None, 'Azure Government is operated by Microsoft': True,
                    'Azure Government is only available to US government agencies and their partners': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/china/overview-operations',
        'explain': """https://docs.microsoft.com/en-us/azure/china/overview-operations 
        https://docs.microsoft.com/en-us/azure/azure-government/documentation-government-welcome""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2165
    },
{'q': """Select all True statements""",
        'options': {'An Azure reource can have multiple Delete locks': True, 'An Azure resource inherits locks from its resource group': True,
                    'If an Azure resource has a Read-Only lock, you can add a Delete lock to the resource': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources',
        'explain': """https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2166
    },
{'q': """Your company plans to migrate all on-premises data to Azure.
You need to identify whether Azure complies with the companyג€™s regional requirements.
What should you use?""",
        'options': {'the Knowledge Center': None, 'Azure Marketplace': None,
                    'the MyApps portal': None, 'the Trust Center': True},
        'explain_url': 'https://azure.microsoft.com/en-gb/overview/trusted-cloud/compliance/',
        'explain': """Azure has more than 90 compliance certifications, including over 50 specific to global regions and countries, such as the US, the European Union, Germany, Japan, the United Kingdom, India and China.

You can view a list of compliance certifications in the Trust Center to determine whether Azure meets your regional requirements.

Reference:
https://azure.microsoft.com/en-gb/overview/trusted-cloud/compliance/ 
https://docs.microsoft.com/en-us/microsoft-365/compliance/get-started-with-service-trust-portal""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2167
    },
{'q': """Select all True statements""",
        'options': {'Authorization to access Azure Resources can be provided only to Azure Active Directory users': None, 'Identities stored in Azure Active Directory, third-party services, and on-premises Active Directory can be used to access Azure resources': True,
                    'Azure has built-in authentication and authorization services that provide secure access to Azure resources': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-fed',
        'explain': """https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-fed""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2168
    },
{'q': """Fill in the blank.  If a resource group named RG1 has a delete lock, _________ can delete RG1""",
        'options': {'only a member of the global administrators group': None, 'the delete lock must be removed before an administrator': True,
                    'an Azure policy must be modified before an administrator': None, 'an Azure tag must be added before an administrator': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-lock-resources',
        'explain': """You can configure a lock on a resource group to prevent the accidental deletion of the resource group. The lock applies to everyone, including global administrators. If you want to delete the resource group, the lock must be removed first.

As an administrator, you may need to lock a subscription, resource group, or resource to prevent other users in your organization from accidentally deleting or modifying critical resources. 

You can set the lock level to CanNotDelete or ReadOnly. In the portal, the locks are called Delete and Read-only respectively.

✑ CanNotDelete means authorized users can still read and modify a resource, but they can't delete the resource.

ReadOnly means authorized users can read a resource, but they can't delete or update the resource. Applying this lock is similar to restricting all authorized users to the permissions granted by the Reader role.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2169
    },
{'q': """Azure Germany can be used by legal residents of Germany only.""",
        'options': {'no change is needed': None, 'only enterprises that are registered in Germany': None,
                    'only enterprises that purchase their azure licenses from a partner based in Germany': None, 'any user or enterprise that requires its data to reside in Germany': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/germany/germany-welcome?toc=%2fazure%2fgermany%2ftoc.json',
        'explain': """Azure Germany is available to eligible customers and partners globally who intend to do business in the EU/EFTA, including the United Kingdom.
        
Azure Germany offers a separate instance of Microsoft Azure services from within German datacenters. The datacenters are in two locations, Frankfurt/Main and
Magdeburg. 

This placement ensures that customer data remains in Germany and that the datacenters connect to each other through a private network. All customer data is exclusively stored in those datacenters. A designated German company--the German data trustee--controls access to customer data and the systems and infrastructure that hold customer data.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2170
    },
{'q': """Select all True statements""",
        'options': {'Identities stored in an on-premises Active directory can be syncronized to Azure Active Directory': True, 'Identities stored in Azure Active Directory, third-party cloud services, and on-premises Active Directory can be used to access Azure resources': True,
                    'Azure has built-in authentication and authoriation services that provide secure access to Azure resources': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-sync-whatis',
        'explain': """Box 1: Yes -
The tool you would use to sync the accounts is Azure AD Connect. The Azure Active Directory Connect synchronization services (Azure AD Connect sync) is a main component of Azure AD Connect. It takes care of all the operations that are related to synchronize identity data between your on-premises environment and
Azure AD.

Box 2: Yes -
As described above, third-party cloud services and on-premises Active Directory can be used to access Azure resources. This is known as ג€˜federationג€™.
Federation is a collection of domains that have established trust. The level of trust may vary, but typically includes authentication and almost always includes authorization. A typical federation might include a number of organizations that have established trust for shared access to a set of resources.

Box 3: Yes -
Azure Active Directory (Azure AD) is a centralized identity provider in the cloud. This is the primary built-in authentication and authorization service to provide secure access to Azure resources.

References:
https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-sync-whatis 
https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-fed 
https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2171
    },
{'q': """Fill in the blank.  You can view your company's regulatory compliance report from __________""",
        'options': {'Azure Advisor': None, 'Azure Analysis Services': None,
                    'Azure Monitor': None, 'Azure Security Center': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/security-center/security-center-intro',
        'explain': """The advanced monitoring capabilities in Security Center lets you track and manage compliance and governance over time. The overall compliance provides you with a measure of how much your subscriptions are compliant with policies associated with your workload.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2172
    },
{'q': """What should you use to evaluate whether your company's Azure environment meets regulatory requirements?""",
        'options': {'Azure Service Health': None, 'Azure Knowledge Center': None,
                    'Azure Security Center': True, 'Azure Advisor': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/security-center/security-center-intro',
        'explain': """The advanced monitoring capabilities in Security Center lets you track and manage compliance and governance over time. The overall compliance provides you with a measure of how much your subscriptions are compliant with policies associated with your workload.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2173
    },
{'q': """Your company has an Azure subscription that contains resources in several regions.
You need to ensure that administrators can only create resources in those regions.

What should you use?""",
        'options': {'a read-only lock': None, 'an Azure policy': True,
                    'a management group': None, ' a reservation': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/policy/overview',
        'explain': """https://docs.microsoft.com/en-us/azure/governance/policy/overview""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2174
    },
{'q': """Select all True statements""",
        'options': {'Azure Active Directory requires the implementation of domain controllers on Azure virtual machines': None, 'Azure Active Directory provides authentication services for resources hosted in Azure and Microsoft 365': True,
                    'Each useer account in Azure Active Directory can be assigned only one license': None},
        'explain_url': '',
        'explain': """Box 1: No -
Azure Active Directory (Azure AD) is a cloud-based service. It does not require domain controllers on virtual machines.

Box 2: Yes -
Azure Active Directory (Azure AD) is a centralized identity provider in the cloud. This is the primary built-in authentication and authorization service to provide secure access to Azure resources and Microsoft 365.

Box 3: No -
User accounts in Azure Active Directory can be assigned multiple licenses for different Azure or Microsoft 365 services.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2175
    },
{'q': """Which two types of customers are eligible to use Azure Government to develop a cloud solution? """,
        'options': {'a Canadian government contractor': None, 'a European government contractor': None,
                    'a United States government entity': True, 'a United States government contractor': True, 'a European government entity': None},
        'explain_url': 'https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-government/2-what-is-azure-government',
        'explain': """Azure Government is a cloud environment specifically built to meet compliance and security requirements for US government. This mission-critical cloud delivers breakthrough innovation to U.S. government customers and their partners. Azure Government applies to government at any level ג€" from state and local governments to federal agencies including Department of Defense agencies.

The key difference between Microsoft Azure and Microsoft Azure Government is that Azure Government is a sovereign cloud. It's a physically separated instance of Azure, dedicated to U.S. government workloads only. It's built exclusively for government agencies and their solution providers.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2176
    },
{'q': """Select all True statements""",
        'options': {'To implement an Azure Multi-Factor Authentication (MFA) solution, you must sync on-premises identities to the cloud': None, 'Two valid methods for Azure Multi-Factor Authentication (MFA) are picture identification and passport number.': None,
                    'Azure Multi-Factor Authentication (MFA) can be required for administive and non-administrative user accounts': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-getstarted',
        'explain': """Box 1: No -
It is not true that you must deploy a federation solution or sync on-premises identities to the cloud. You can have a cloud-only environment and use MFA.

Box 2: No -
Picture identification and passport numbers are not valid MFA authentication methods. Valid methods include: Password, Microsoft Authenticator App, SMS and Voice call.

Box 3:
You can configure MFA to be required for administrator accounts only or you can configure MFA for any user account.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2177
    },
{'q': """You need to ensure that when Azure Active Directory (Azure AD) users connect to Azure AD from the Internet by using an anonymous IP address, the users are prompted automatically to change their password.
Which Azure service should you use?""",
        'options': {'Azure AD Connect Health': None, 'Azure AD Privileged Identity Management': None,
                    'Azure Advanced Threat Protection (ATP)': None, 'Azure AD Identity Protection': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/howto-sign-in-risk-policy',
        'explain': """Azure AD Identity Protection includes two risk policies: sign-in risk policy and user risk policy. A sign-in risk represents the probability that a given authentication request isnג€™t authorized by the identity owner.

There are several types of risk detection. One of them is Anonymous IP Address. This risk detection type indicates sign-ins from an anonymous IP address (for example, Tor browser or anonymous VPN). These IP addresses are typically used by actors who want to hide their login telemetry (IP address, location, device, etc.) for potentially malicious intent.

You can configure the sign-in risk policy to require that users change their password.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2178
    },
{'q': """Matching""",
        'options': {'ISO': 'An organization that defines international standards across all industries', 'NIST': 'An organization that defines standards used by the US goverment',
                    'GDPR': 'A European policy that regulates data privacy and data protection', 'Azure Government': 'A dedicated public cloud for federal and state agencies in the United States'},
        'explain_url': 'https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology',
        'explain': """Box 1: ISO -
ISO is the International Organization for Standardization. Companies can be certified to ISO standards, for example ISO 9001 or 27001 are commonly used in IT companies.

Box 2: NIST -
The National Institute of Standards and Technology (NIST) is a physical sciences laboratory, and a non-regulatory agency of the United States Department of
Commerce.

Box 3: GDPR -
GDPR is the General Data Protection Regulations. This standard was adopted across Europe in May 2018 and replaces the now deprecated Data Protection
Directive.
The General Data Protection Regulation (EU) (GDPR) is a regulation in EU law on data protection and privacy in the European Union (EU) and the European
Economic Area (EEA). It also addresses the transfer of personal data outside the EU and EEA areas. The GDPR aims primarily to give control to individuals over their personal data and to simplify the regulatory environment for international business by unifying the regulation within the EU.

Box 4: Azure Government -
US government agencies or their partners interested in cloud services that meet government security and compliance requirements, can be confident that
Microsoft Azure Government provides world-class security, protection, and compliance services. Azure Government delivers a dedicated cloud enabling government agencies and their partners to transform mission-critical workloads to the cloud. Azure Government services handle data that is subject to certain government regulations and requirements, such as FedRAMP, NIST 800.171 (DIB), ITAR, IRS 1075, DoD L4, and CJIS. In order to provide you with the highest level of security and compliance, Azure Government uses physically isolated datacenters and networks (located in U.S. only).""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'match',
        'id': 2179
    },
{'q': """To what should an application connect to retrieve security tokens?""",
        'options': {'an Azure Storage account': None, 'Azure Active Directory (Azure AD)': True,
                    'a certificate store': None, 'n Azure key vault': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios',
        'explain': """Azure AD authenticates users and provides access tokens. An access token is a security token that is issued by an authorization server. It contains information about the user and the app for which the token is intended, which can be used to access Web APIs and other protected resources.

Instead of creating apps that each maintain their own username and password information, which incurs a high administrative burden when you need to add or remove users across multiple apps, apps can delegate that responsibility to a centralized identity provider.

Azure Active Directory (Azure AD) is a centralized identity provider in the cloud. Delegating authentication and authorization to it enables scenarios such as

Conditional Access policies that require a user to be in a specific location, the use of multi-factor authentication, as well as enabling a user to sign in once and then be automatically signed in to all of the web apps that share the same centralized directory. This capability is referred to as Single Sign On (SSO).""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2180
    },
{'q': """Your network contains an Active Directory forest. The forest contains 5,000 user accounts.
Your company plans to migrate all network resources to Azure and to decommission the on-premises data center.

You need to recommend a solution to minimize the impact on users after the planned migration.
What should you recommend?""",
        'options': {'Implement Azure Multi-Factor Authentication (MFA)': None, 'Sync all the Active Directory user accounts to Azure Active Directory (Azure AD)': True,
                    'Instruct all users to change their password': None, 'Create a guest user account in Azure Active Directory (Azure AD) for each user': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-sync-whatis',
        'explain': """To migrate to Azure and decommission the on-premises data center, you would need to create the 5,000 user accounts in Azure Active Directory. The easy way to do this is to sync all the Active Directory user accounts to Azure Active Directory (Azure AD). You can even sync their passwords to further minimize the impact on users.

The tool you would use to sync the accounts is Azure AD Connect. The Azure Active Directory Connect synchronization services (Azure AD Connect sync) is a main component of Azure AD Connect. It takes care of all the operations that are related to synchronize identity data between your on-premises environment and Azure AD.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2181
    },
{'q': """Select all True statements""",
        'options': {'You can configure the Azure Active Directory activity logs to appear in Azure Monitor': True, 'From Azure Monitor, you can monitor across multiple subscriptions': True,
                    'From Azure Monitor, you can create alerts': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-activity-logs-azure-monitor',
        'explain': """Box 1: Yes -
You can send Azure AD activity logs to Azure Monitor logs to enable rich visualizations, monitoring and alerting on the connected data.

All data collected by Azure Monitor fits into one of two fundamental types, metrics and logs (including Azure AD activity logs). Activity logs record when resources are created or modified. Metrics tell you how the resource is performing and the resources that it's consuming.

Box 2: Yes -
Azure Monitor can consolidate log entries from multiple Azure resources, subscriptions, and tenants into one location for analysis together.

Box 3: Yes -
You can create alerts in Azure Monitor.
Alerts in Azure Monitor proactively notify you of critical conditions and potentially attempt to take corrective action. Alert rules based on metrics provide near real time alerting based on numeric values, while rules based on logs allow for complex logic across data from multiple sources.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'multi',
        'id': 2182
    },
{'q': """You create a resource group named RG1 in Azure Resource Manager.
You need to prevent the accidental deletion of the resources in RG1.
Which setting should you use?""",
        'options': {'Policies': None, 'Locks': True,
                    'Properties': None, 'Automation script': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-lock-resources',
        'explain': """You can configure a lock on a resource group to prevent the accidental deletion.

As an administrator, you may need to lock a subscription, resource group, or resource to prevent other users in your organization from accidentally deleting or modifying critical resources. You can set the lock level to CanNotDelete or ReadOnly. In the portal, the locks are called Delete and Read-only respectively.

CanNotDelete means authorized users can still read and modify a resource, but they can't delete the resource.✑ ReadOnly means authorized users can read a resource, but they can't delete or update the resource. Applying this lock is similar to restricting all authorized users to the permissions granted by the Reader role.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2183
    },
{'q': """You have a resource group named RG1.
You need to prevent the creation of virtual machines only in RG1. The solution must ensure that other objects can be created in RG1.
What should you use?""",
        'options': {'a lock': None, 'an Azure role': None,
                    'a tag': None, 'an Azure policy': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/governance/policy/overview',
        'explain': """Azure policies can be used to define requirements for resource properties during deployment and for already existing resources. Azure Policy controls properties such as the types or locations of resources.

Azure Policy is a service in Azure that you use to create, assign, and manage policies. These policies enforce different rules and effects over your resources, so those resources stay compliant with your corporate standards and service level agreements.

In this question, we would create an Azure policy assigned to the resource group that denies the creation of virtual machines in the resource group.

You could place a read-only lock on the resource group. However, that would prevent the creation of any resources in the resource group, not virtual machines only. Therefore, an Azure Policy is a better solution.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'basic',
        'id': 2184
    },
{'q': """Select all True statements""",
        'options': {'Storing 1 TB of data in Azure Blob storage will always cost the same, regardless of the Azure region in which the data is located': None, 'When you use a general-purpose v2 Azure Storage account, you are only charged for the amount of data that is stored. All read and write operations are free': None,
                    'Transferring data between Azure Storage accounts in different Azure regions is free': None},
        'explain_url': """https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview""",
        'explain': """Box 1: No -
The price of Azure storage varies by region. If you use the Azure storage pricing page, you can select different regions and see how the price changes per region.

Box 2: No -
You are charged for read and write operations in general-purpose v2 storage accounts.

Box 3: No -
You would be charge for the read operations of the source storage account and write operations in the destination storage account.

https://azure.microsoft.com/en-gb/pricing/details/storage/blobs/""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2185
    },
{'q': """Select all True statements""",
        'options': {'In Azure Active Directory Premium P2, at least 99.9% availability is guaranteed': True, 'The SLA for Azure Active Directory Premium P2 is the same as the SLA for Azure Active Directory Free': None,
                    'All paying Azure customers receive a credit if their monthly uptime percentage is below the guarenteed amount in the SLA': True},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/legal/sla/active-directory/v1_0/',
        'explain': """Box 1: Yes -
Microsoft guarantee at least 99.9% availability of the Azure Active Directory Premium edition services. The services are considered available in the following scenarios:
✑ Users are able to login to the service, login to the Access Panel, access applications on the Access Panel and reset passwords.
✑ IT administrators are able to create, read, write and delete entries in the directory or provision or de-provision users to applications in the directory.

Box 2: No -
No SLA is provided for the Free tier of Azure Active Directory.

Box 3: Yes -
You can claim credit if the availability falls below the SLA. The amount of credit depends on the availability. For example: You can claim 25% credit if the availability is less than 99.9%, 50% credit for less than 99% and 100% for less than 95% availability.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2186
    },
{'q': """Select all True statements""",
        'options': {'Adding resource groups in the Azure subscription generates additional costs': None, 'Copying 10 GB of data TO Azure FROM an on-premises network over a VPN generates additional Azure data ctransfer costs': None,
                    'Copying 10 GB of data FROM Azure TO an on-premises network over a VPN generates addition': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/manage-resource-groups-portal',
        'explain': """Box 1: No -
Resource groups are logical containers for Azure resources. You do not pay for resource groups.

Box 2: No -
Data ingress over a VPN is data ג€˜coming in to Azure over the VPN. You are not charged data transfer costs for data ingress.

Box 3: Yes -
Data egress over a VPN is data going out of Azure over the VPN. You are charged for data egress.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2187
    },
{'q': """Fill in the blank.  Yu deploy an Azure resource.  The resource becomes unavailable for an extended period dur to a service outage.  Microsoft will __________""",
        'options': {'refund your bank account': None, 'migrate the resource to another subscription': None,
                    'credit your Azure account': True, 'send you a coupon code that you can redeem for Azure credits': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/legal/sla/analysis-services/v1_0/',
        'explain': """If the SLA for an Azure service is not met, you receive credits for that service and that service only. The credits are deducted from your monthly bill for that service.

If you stopped using the service where the SLA was not met, your account would remain in credit for that service. The credits would not be applied to any other services that you may be using.

Service Credits apply only to fees paid for the particular Service, Service Resource, or Service tier for which a Service Level has not been met. In cases where

Service Levels apply to individual Service Resources or to separate Service tiers, Service Credits apply only to fees paid for the affected Service Resource or

Service tier, as applicable. The Service Credits awarded in any billing month for a particular Service or Service Resource will not, under any circumstance, exceed your monthly service fees for that Service or Service Resource, as applicable, in the billing month.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2188
    },
{'q': """Which task can you perform by using Azure Advisor?""",
        'options': {' Integrate Active Directory and Azure Active Directory (Azure AD).': None, 'Estimate the costs of an Azure solution.': True,
                    'Confirm that Azure subscription security follows best practices.': None, 'Evaluate which on-premises resources can be migrated to Azure.': None},
        'explain_url': 'https://blog.pragmaticworks.com/what-is-azure-advi-sor#:~:text=Microsoft%20defines%20Azure%20Advisor%20as,solutions%20based%20on%20that%20data',
        'explain': """.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2189
    },

{'q': """Select all True statements""",
        'options': {'If your company uses an Azure free account, you will only be able to use a subset of Azure services': None, 'All Azure free accounts expire after a specific period': True,
                    'You can create up to 10 Azure free accounts by using the same Microsoft account': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/free/',
        'explain': """Box 1: No -
Azure Free Account gives you 12 months access to the most popular free services. It also gives you a credit (150 GBP or 200 USD) to use on any Azure service for up to 30 days.

Box 2: Yes -
All free accounts expire after 12 months.

Box 3: No -
You can only create one free Azure account per Microsoft account.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2190
    },
{'q': """Select all True statements""",
        'options': {'All Azure services in private preview must be accessed by using a separate portal': None, 'Azure services in public preview can be used in production environments': True,
                    'Azure services in public preview are subject to an SLA': None},
        'explain_url': 'https://www.neowin.net/news/several-more-azure-services-now-available-in-private-public-preview/',
        'explain': """Public Preview means that the service is in public beta and can be tried out by anyone with an Azure subscription. Services in public preview are often offered at a discount price.

Box 1: No -
Services in private preview can be viewed in the regular Azure portal. However, you need to be signed up for the feature in private preview before you can view it.
Access to private preview features is usually by invitation only.

Box 2: Yes -
You can use services in public preview in production environments. However, you should be aware that the service may have faults, is not subject to an SLA and may be withdrawn without notice.

Box 3: No -
Public previews are excluded from SLAs and in some cases, no support is offered.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2191
    },
{'q': """Your company has 10 offices. You plan to generate several billing reports from the Azure portal. Each report will contain the Azure resource utilization of each office.
Which Azure Resource Manager feature should you use before you generate the reports?""",
        'options': {'tags': True, 'templates': None,
                    'locks': None, 'policies': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/',
        'explain': """You can use resource tags to label Azure resources. Tags are metadata elements attached to resources. Tags consist of pairs of key/value strings. In this question, we would tag each resource with a tag to identify each office. For example: Location = Office1. When all Azure resources are tagged, you can generate reports to list all resources based on the value of the tag. For example: All resources used by Office1.""",
        'notes': '',
        'history': '',
        'category': 'identity',
        'q_type': 'cost',
        'id': 2192
    },
{'q': """Select all True statements""",
        'options': {'A Standard support plan is included in an Azure Free account': None, 'A Premier support plan can only be purchased by companies that have an Enterprise Agreement (EA)': True,
                    'Support from MSDN fourms is only provided to companies that have a pay-as-you-go subscription': None},
        'explain_url': 'https://azure.microsoft.com/en-us/support/plans/',
        'explain': """Box 1: No -
An Azure free account comes with a ג€˜basicג€™ support plan, not a ג€˜standardג€™ support plan.

Box 2: Yes -
You can purchase the Professional Direct, Standard, and Developer support plans with the Microsoft Customer Agreement. You can also purchase the
Professional and Standard support plans with the Enterprise Agreement.

Box 3: No -
Users with any type of Azure subscription (pay-as-you-go, Enterprise Agreement, Microsoft Customer Agreement etc.) can get support from the MSDN forums.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2193
    },
{'q': """If Microsoft plans to end support for an Azure service that does NOT have a successor service, Microsoft will provide notification at least 12 months before.""",
        'options': {'No change is needed.': True, '6 months': None,
                    '90 days': None, '30 days': None},
        'explain_url': 'https://support.microsoft.com/en-us/help/30881',
        'explain': """The Modern Lifecycle Policy covers products and services that are serviced and supported continuously. For products governed by the Modern Lifecycle Policy,

Microsoft will provide a minimum of 12 months' notification prior to ending support if no successor product or service is offeredג€"excluding free services or preview releases.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2194
    },
{'q': """Select all True statements""",
        'options': {'A user who is assigned the Owner role can transfer ownership of an Azure subscription': None, 'You can convert the Azure subscription of your company from Free Trial to Pay-as-you-go': True,
                    'The Azure spending limit is fixed and cannot be increased or decreased': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/billing/billing-add-change-azure-subscription-administrator',
        'explain': """Box 1: No -
You need to be an administrator of the billing account that has the subscription to be able to transfer the subscription. This could be a Billing Administrator or

Global Administrator. A subscription owner can manage all resources and permissions within the subscription but cannot transfer ownership of the subscription.

Box 2: Yes -
You can convert a free trial subscription to Pay-As-You-Go. This is common practice for people who wish to continue using the Azure services when the free trial period expires.

Box 3: Yes -
You can remove the spending limit, but you canג€™t increase or decrease it.
The spending limit in Azure prevents spending over your credit amount. All new customers who sign up for an Azure free account or subscription types that include credits over multiple months have the spending limit turned on by default. The spending limit is equal to the amount of credit and it canג€™t be changed. For example, if you signed up for Azure free account, your spending limit is $200 and you can't change it to $500. However, you can remove the spending limit. So, you either have no limit, or you have a limit equal to the amount of credit.

Reference:
https://docs.microsoft.com/en-us/azure/billing/billing-add-change-azure-subscription-administrator 
https://docs.microsoft.com/en-us/azure/billing/billing-upgrade-azure-subscription 
https://docs.microsoft.com/en-us/azure/billing/billing-spending-limit""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2195
    },
{'q': """Select all True statements""",
        'options': {'With Azure Reservations, you pay less for VMs than with pay-as-you-go pricing': True, 'Two Azure VMs that use the B2S size have the same monthly storage costs': None,
                    'When an Azure virtual machine is stopped, you continue to pay storage costs for the VM': True},
        'explain_url': 'https://azure.microsoft.com/en-us/reservations/',
        'explain': """https://azure.microsoft.com/en-us/reservations/""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2196
    },
{'q': """After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.
Your company has an Azure subscription that contains the following unused resources:
✑ 20 user accounts in Azure Active Directory (Azure AD)
✑ Five groups in Azure AD
✑ 10 public IP addresses
✑ 10 network interfaces

You need to reduce the Azure costs for the company.

Solution: You remove the unused network interfaces.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations#reduce-costs-by-deleting-or-reconfiguring-idle-virtual-network-gateways',
        'explain': """https://docs.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations#reduce-costs-by-deleting-or-reconfiguring-idle-virtual-network-gateways""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2197
    },
{'q': """Your company has an Azure subscription that contains the following unused resources:
20 user accounts in Azure Active Directory (Azure AD)
✑ Five groups in Azure AD
✑ 10 public IP addresses
✑ 10 network interfaces

You need to reduce the Azure costs for the company.

Solution: You remove the unused public IP addresses.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations#reduce-costs-by-deleting-or-reconfiguring-idle-virtual-network-gateways',
        'explain': """You are charged for public IP addresses. Therefore, deleting unused public IP addresses will reduce the Azure costs.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2198
    },
{'q': """Your company has an Azure subscription that contains the following unused resources:
✑ 20 user accounts in Azure Active Directory (Azure AD)
✑ Five groups in Azure AD
✑ 10 public IP addresses
✑ 10 network interfaces

You need to reduce the Azure costs for the company.
Solution: You remove the unused user accounts.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations#reduce-costs-by-deleting-or-reconfiguring-idle-virtual-network-gateways',
        'explain': """You are not charged for user accounts. Therefore, deleting unused user accounts will not reduce the Azure costs for the company.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2199
    },
{'q': """How should you calculate the monthly uptime percentage?""",
        'options': {'Downtime in minutes / 60 X 100': None, 'Downtime in minutes / 1440 X 99.99': None,
                    '(Maximum Avail Minutes - Downtime minutes) / Maximum avail minutes x 100': True},
        'explain_url': 'https://azure.microsoft.com/en-au/support/legal/sla/cloud-services/v1_0/',
        'explain': """"Maximum Available Minutes" is the total accumulated minutes during a billing month .

"Downtime" is the total accumulated minutes that are part of Maximum Available Minutes where a system is unavailable.

"Monthly Uptime Percentage" for a service is calculated as Maximum Available Minutes less Downtime divided by Maximum Available Minutes x 100.

Monthly Uptime Percentage is represented by the following formula:

Monthly Uptime % = (Maximum Available Minutes-Downtime) / Maximum Available Minutes x 100.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2200
    },
    {'q': """Select all True statements""",
        'options': {'By creating additional resource groups in an Azure subscription, additional costs are incurred': None, 'By copying several gigabits of data TO Azure from an on-premises network over a VPN, additional data transfer costs are incurred': None,
                    'By copying several GB of data FROM Azure TO an on-premises network over a VPN, additional data transfer costs are incurred': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-resource-manager/manage-resource-groups-portal',
        'explain': """Box 1: No -
Resource groups are logical containers for Azure resources. You do not pay for resource groups.

Box 2: No -
Data ingress over a VPN is data incoming to Azure over the VPN. You are not charged data transfer costs for data ingress.

Box 3: Yes -
Data egress over a VPN is data going out of Azure over the VPN. You are charged for data egress.

Reference:
https://docs.microsoft.com/en-us/azure/azure-resource-manager/manage-resource-groups-portal 
https://azure.microsoft.com/en-us/pricing/details/bandwidth/
 https://azure.microsoft.com/en-us/pricing/details/bandwidth/""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2201
        },
{'q': """A support plan solution that gives you best practice information, health status and notifications, and 24/7 access to billing information at the lowest possible cost is a Standard support plan.""",
        'options': {'No change is needed': None, 'Developer': None,
                    'Basic': True, 'Premier': None},
        'explain_url': 'https://azure.microsoft.com/en-us/support/plans/',
        'explain': """A basic support plan provides:
        
✑ 24x7 access to billing and subscription support, online self-help, documentation, whitepapers, and support forums
✑ Best practices: Access to full set of Azure Advisor recommendations
✑ Health Status and Notifications: Access to personalized Service Health Dashboard & Health API""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2202
        },
{'q': """In which Azure support plans can you open a new support request?""",
        'options': {'Premier and Professional Direct only': None, 'Premier, Professional Direct, and Standard only': None,
                    'Premier, Professional Direct, Standard, and Developer only': True, 'Premier, Professional Direct, Standard, Developer, and Basic': None},
        'explain_url': 'https://azure.microsoft.com/en-us/support/plans/',
        'explain': """You can open support cases in the following plans: Premier, Professional Direct, Standard, and Developer only.
You cannot open support cases in the Basic support plan.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2203
        },
{'q': """You can create an Azure support request from support.microsoft.com.""",
        'options': {'No change is needed.': None, ' the Azure portal': True,
                    'the Knowledge Center': None, 'the Security & Compliance admin center': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-supportability/how-to-create-azure-support-request',
        'explain': """You can create an Azure support request from the Help and Support blade in the Azure portal or from the context menu of an Azure resource in the Support + Troubleshooting section.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2204
        },
{'q': """Your company has an Azure subscription that contains the following unused resources:
✑ 20 user accounts in Azure Active Directory (Azure AD)
✑ Five groups in Azure AD
✑ 10 public IP addresses
✑ 10 network interfaces

You need to reduce the Azure costs for the company.

Solution: You remove the unused groups.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations#reduce-costs-by-deleting-or-reconfiguring-idle-virtual-network-gateways',
        'explain': """You are not charged for Azure Active Directory Groups. Therefore, deleting unused groups will not reduce your Azure costs.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2205
        },
{'q': """The Azure Standard support plan is the lowest cost option to receive 24x7 access to support engineers by phone.""",
        'options': {'No change is needed': True, 'Developer': None,
                    'Basic': None, 'Professional Direct': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/plans/',
        'explain': """The Basic support plan is free so is therefore the cheapest. The Developer support plan is the cheapest paid-for support plan. The order of support plans in terms of cost ranging from the cheapest to most expensive is: Basic, Developer, Standard, Professional Direct, Premier.

However, 24/7 access to technical support by email and phone is only available for Standard, Professional Direct, Premier plans.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2206
        },
{'q': """Fill in the blank. All Azure services that are in public preview are ___________""",
        'options': {'provided without any documentation': None, 'only configurable from Azure CLI': None,
                    'excluded from the Service Level Agreements': True, 'only configurable from Azure Portal': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/legal/preview-supplemental-terms/',
        'explain': """Preview features are made available to you on the condition that you accept additional terms which supplement the regular Azure terms. The supplemental terms state:
PREVIEWS ARE PROVIDED "AS-IS," 
"WITH ALL FAULTS," AND "AS AVAILABLE," 
AND ARE EXCLUDED FROM THE SERVICE LEVEL AGREEMENTS AND LIMITED WARRANTY.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2207
        },
{'q': """Fill in the blank.  An Azure service is available to all Azure customers when it is in _______________""",
        'options': {'public preview': None, 'private preview': None,
                    'development': None, 'an Enterprise Agreement (EA)': None},
        'explain_url': 'https://www.neowin.net/news/several-more-azure-services-now-available-in-private-public-preview/',
        'explain': """Public Preview means that the service is in public beta and can be tried out by anyone with an Azure subscription. Services in public preview are often offered at a discount price.

Public previews are excluded from SLAs and in some cases, no support is offered.

Incorrect Answers:
✑ Services in private preview are available only to selected people who has signed up to the private preview program.
✑ Services in development are not available to the public.
✑ Services provided under an Enterprise Agreement (EA) subscription are available only to the subscription owner.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2209
        },
{'q': """What is guaranteed in an Azure Service Level Agreement (SLA) for virtual machines?""",
        'options': {'uptime': True, 'feature availability': None,
                    'bandwidth': None, 'performance': None},
        'explain_url': 'https://azure.microsoft.com/en-us/support/legal/sla/summary/',
        'explain': """The SLA for virtual machines guarantees ג€˜uptimeג€™. The amount of uptime guaranteed depends on factors such as whether the VMs are in an availability set or availability zone if there is more than one VM, the distribution of the VMs if there is more than one or the disk type if it is a single VM.

The SLA for Virtual Machines states:
✑ For all Virtual Machines that have two or more instances deployed across two or more Availability Zones in the same Azure region, we guarantee you will have

Virtual Machine Connectivity to at least one instance at least 99.99% of the time.
✑ For all Virtual Machines that have two or more instances deployed in the same Availability Set or in the same Dedicated Host Group, we guarantee you will have Virtual Machine Connectivity to at least one instance at least 99.95% of the time.
✑ For any Single Instance Virtual Machine using Premium SSD or Ultra Disk for all Operating System Disks and Data Disks, we guarantee you will have Virtual

Machine Connectivity of at least 99.9%.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2208
        },
{'q': """Your company plans to purchase an Azure subscription.
The company's support policy states that the Azure environment must provide an option to access support engineers by phone or email.
You need to recommend which support plan meets the support policy requirement.

Solution: Recommend a Basic support plan.
Does this meet the goal?""",
        'options': {'Yes': None, 'No': True},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/plans/',
        'explain': """The Basic support plan does not have any technical support for engineers.

Access to Support Engineers via email or phone is available in the following support plans: Premier, Professional Direct and standard.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2210
        },
{'q': """Your company plans to purchase an Azure subscription.
The company's support policy states that the Azure environment must provide an option to access support engineers by phone or email.
You need to recommend which support plan meets the support policy requirement.

Solution: Recommend a Standard support plan.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/plans/',
        'explain': """The Standard, Professional Direct, and Premier support plans have technical support for engineers via email and phone.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2211
        },
{'q': """Your company plans to purchase an Azure subscription.
The company's support policy states that the Azure environment must provide an option to access support engineers by phone or email.
You need to recommend which support plan meets the support policy requirement.

Solution: Recommend a Premier support plan.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/plans/',
        'explain': """The Standard, Professional Direct, and Premier support plans have technical support for engineers via email and phone.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2212
        },
{'q': """The company currently has a Basic support plan.
You need to recommend a new support plan for the company. The solution must minimize costs.

Which support plan should you recommend?""",
        'options': {'Premier': True, 'Developer': None,
                    'Professional Direct': None, 'Standard': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/plans/',
        'explain': """https://azure.microsoft.com/en-gb/support/plans/""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2213
        },
{'q': """Select all True statements""",
        'options': {'Most Azure services are introduced in private preview before being introduced to public preview, and then in general availability': True, 'Azure services in public preview can be managed only by using the Azure CLI': None,
                    'The cost of an Azure service in private preview decreases when the service becomes generally available': None},
        'explain_url': '',
        'explain': """Box 1: Yes -
Most services go to private preview then public preview before being released to general availability.
The private preview is only available to certain Azure customers for evaluation purposes. The public preview is available to all Azure customers.

Box 2: No -
Azure services in public preview can be managed using the regular management tools: Azure Portal, Azure CLI and PowerShell.

Box 3: No -
Services in private or public preview are usually offered at reduced costs. However, the costs increase, not decrease when the services are released to general availability.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2214
        },
{'q': """What is required to use Azure Cost Management?""",
        'options': {'a Dev/Test subscription': None, 'Software Assurance': None,
                    'an Enterprise Agreement (EA)': True, 'a pay-as-you-go subscription': None},
        'explain_url': 'https://docs.microsoft.com/en-gb/azure/cost-management/overview-cost-mgt',
        'explain': """Azure customers with an Azure Enterprise Agreement (EA), Microsoft Customer Agreement (MCA), or Microsoft Partner Agreement (MPA) can use Azure Cost Management.

Cost management is the process of effectively planning and controlling costs involved in your business. Cost management tasks are normally performed by finance, management, and app teams. Azure Cost Management + Billing helps organizations plan with cost in mind. It also helps to analyze costs effectively and take action to optimize cloud spending.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2215
        },
{'q': """Fill in the blank.  Your Azure trial account expired last week. You are now unable to __________""",
        'options': {'Create additional Azure AD users': None, 'start an existing Azure VM': True,
                    'access your data store in Azure': None, 'access the Azure Portal': None},
        'explain_url': '',
        'explain': """A stopped (deallocated) VM is offline and not mounted on an Azure host server. Starting a VM mounts the VM on a host server before the VM starts. As soon as the VM is mounted, it becomes chargeable. For this reason, you are unable to start a VM after a trial has expired.

Incorrect Answers:
✑ You are not charged for Azure Active Directory user accounts so you can continue to create accounts.
✑ You can access data that is already stored in Azure.
✑ You can access the Azure Portal. You can also reactivate and upgrade the expired subscription in the portal.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2216
        },
{'q': """Your company plans to purchase an Azure subscription.
The company's support policy states that the Azure environment must provide an option to access support engineers by phone or email.
You need to recommend which support plan meets the support policy requirement.

Solution: Recommend a Professional Direct support plan.
Does this meet the goal?""",
        'options': {'Yes': True, 'No': None},
        'explain_url': 'https://azure.microsoft.com/en-gb/support/plans/',
        'explain': """The Basic support plan does not have any technical support for engineers.

The Developer support plan has only technical support for engineers via email.

The Standard, Professional Direct, and Premier support plans have technical support for engineers via email and phone.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2217
        },
{'q': """Your company has a Software Assurance agreement that includes Microsoft SQL Server licenses.
You plan to deploy SQL Server on Azure virtual machines.
What should you do to minimize licensing costs for the deployment?""",
        'options': {'Deallocate the virtual machines during off hours.': None, 'Use Azure Hybrid Benefit.': None,
                    'Configure Azure Cost Management budgets.': None, 'Use Azure reservations.': None},
        'explain_url': 'https://azure.microsoft.com/en-us/pricing/hybrid-benefit/',
        'explain': """Azure Hybrid Benefit is a licensing benefit that helps you to significantly reduce the costs of running your workloads in the cloud. It works by letting you use your on-premises Software Assurance-enabled Windows Server and SQL Server licenses on Azure.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2218
        },
{'q': """Your company has 10 departments.
The company plans to implement an Azure environment.
You need to ensure that each department can use a different payment option for the Azure services it consumes.
What should you create for each department?""",
        'options': {'a reservation': None, 'a subscription': True,
                    'a resource group': None, 'a container instance': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription',
        'explain': """There are different payment options in Azure including pay-as-you-go (PAYG), Enterprise Agreement (EA), and Microsoft Customer Agreement (MCA) accounts.
Your Azure costs are per subscription. You are charged monthly for all resources in a subscription. Therefore, to use different payment options per department, you will need to create a separate subscription per department. You can create multiple subscriptions in a single Azure Active Directory tenant.

Incorrect Answers:
A: A reservation is where you commit to a resource (for example a virtual machine) for one or three years. This gives you a discounted price on the resource for the reservation period. Reservations do not provide a way to use different payment options per department.

C: A resource group is a logical container for Azure resources. You can view the total cost of all the resources in a resource group. However, resource groups do not provide a way to use different payment options per department.

D: A container instance is an Azure resource used to run an application. Container instances do not provide a way to use different payment options per department.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2219
        },
{'q': """Select all True statements""",
        'options': {'An Azure Free account has a spending limit': True, 'An Azure Free account has a limit of 2 TB of data that can be uploaded to Azure': None,
                    'An Azure Free account can contain an unlimited number of web apps': None},
        'explain_url': 'https://azure.microsoft.com/en-us/free/free-account-faq/',
        'explain': """An Azure free account has a spending limit. This is currently 200 USD or 150 GBP.

Box 2: No -
Azure free account has a 5 GB blob storage limit and a 5 GB file storage limit.

Box 3: No -
Azure free account has a limit of 10 web, mobile or API apps""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2220
        },
{'q': """Select all True statements""",
        'options': {'An Azure service in private preview is released to all Azure customers': None, 'An Azure service in public preview is released to all Azure customers': True,
                    'An Azure service in general availability is released to a subset of Azure customers': None},
        'explain_url': 'https://azure-overview.com/Home/Faq',
        'explain': """Box 1: No -
Most services go to private preview then public preview before being released to general availability. The private preview is only available to certain Azure customers for evaluation purposes.

Box 2: Yes -
Public Preview means that the service is in public beta and can be tried out by anyone with an Azure subscription. Services in public preview are often offered at a discount price.
Public previews are excluded from SLAs and in some cases, no support is offered.

Box 3: No -
An Azure service in general availability is available to all Azure customers, not just a subset of the customers.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2221
        },
{'q': """Select all True statements""",
        'options': {'With a consumption-based plan, you pay a fixed rate for all data sent to of from virtual machines hosted in the cloud': None, 'With a consumption-based plan, you reduce overall costs by paying only for extra capacity when it is required.': True,
                    'Serverless computing is an example of a consumption-based pan': True},
        'explain_url': '',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2222
        },
{'q': """Select all True statements""",
        'options': {'The cost of Azure resources can vary between regions': True, 'An Azure reservation is used to reserve server capacity at a specific data center': True,
                    'You can stop an Azure SQL Database instance to decrease costs': None},
        'explain_url': '',
        'explain': """""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2223
        },
{'q': """Fill in the blank.  You have an application that is comprised of an Azure web app that has a Service Level Agreement (SLA) of 99.95 percent and an Azure SQL database that has an SQL of 99.99 percent.  The composite SQL for the application is _______ """,
        'options': {'the product of both SLAs, which is 99.94 percent': True, 'the lowest SLA associated to the application, which is 99.95 percent': None,
                    'The highest SLA associated to the application, which is 99.99 percent': None, 'the difference between the to SLAs, which is 0.05 persent': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/architecture/reliability/requirements#understand-service-level-agreements',
        'explain': """Composite SLAs involve multiple services supporting an application, each with differing levels of availability. 
        
        For example, consider an App Service web app that writes to Azure SQL Database. At the time of this writing, these Azure services have the following SLAs:

✑ App Service web apps = 99.95%

✑ SQL Database = 99.99%

What is the maximum downtime you would expect for this application? If either service fails, the whole application fails. The probability of each service failing is independent, so the composite SLA for this application is 99.95% ֳ— 99.99% = 99.94%. That's lower than the individual SLAs, which isn't surprising because an application that relies on multiple services has more potential failure points.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2224
        },
{'q': """Select all True statements""",
        'options': {'The Service Level Agreement (SLA) guaranteed uptime for paid Azure services is at least 99.9 percent': None, 'Companies can increase the Service Level Agreement (SLA) guaranteed uptime by adding Azure resources to multiple regions': None,
                    'Companies can increase the Service Level Agreement (SLA) guaranteed uptime by purchasing multiple subscriptions': None},
        'explain_url': 'https://azure.microsoft.com/en-us/support/legal/sla/summary/',
        'explain': """Box 1: Yes -
SLAs vary based on the resource type and the location distribution of the resource. However, the minimum uptime for all Azure services is 99.9 percent.

Box 2: Yes -
The SLA guaranteed uptime is increased (usually to 99.95 percent) when resources are deployed across multiple regions.

Box 3: No -
The number of subscriptions is unrelated to uptime SLAs. You can deploy resources to multiple regions under a single subscription or you can have multiple subscriptions with resources deployed to the same region.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'multi',
        'id': 2225
        },
{'q': """Which statement accurately describes the Modern Lifecycle Policy for Azure services?""",
        'options': {'Microsoft provides mainstream support for a service for five years.': None, 'Microsoft provides a minimum of 12 monthsג€™ notice before ending support for a service.': True,
                    'After a service is made generally available, Microsoft provides support for the service for a minimum of four years.': None, 'When a service is retired, you can purchase extended support for the service for up to five years.': None},
        'explain_url': 'https://support.microsoft.com/en-us/help/30881/modern-lifecycle-policy',
        'explain': """For products governed by the Modern Lifecycle Policy, Microsoft will provide a minimum of 12 months' notification prior to ending support if no successor product or service is offered ג€" excluding free services or preview releases.""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2226
        },
{'q': """You need to request that Microsoft increase a subscription quota limit for your company.
Which blade should you use from the Azure portal?""",
        'options': {'No idea': None, 'can see the picture': None,},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/azure-portal/supportability/per-vm-quota-requests',
        'explain': """Request a standard quota increase from Help + support""",
        'notes': '',
        'history': '',
        'category': 'cost',
        'q_type': 'basic',
        'id': 2227
        },
{'q': """Fill in the blank.  You can use _____________ in Azure to send email alerts when the cost of the current billing period for an Azure subscription exceeds a specific limit""",
        'options': {'Advisor recommendations': None, 'Access control (IAM)': None,
                    'Budget alerts': True, 'Compliance': None},
        'explain_url': 'https://docs.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending',
        'explain': """Budget alerts notify you when spending, based on usage or cost, reaches or exceeds the amount defined in the alert condition of the budget. Cost Management budgets are created using the Azure portal or the Azure Consumption API.""",
        'notes': '',
        'history': '',
        # 'category': 'cost',
        'category': 'test',
        'q_type': 'basic',
        'id': 2228
        },
{'q': """Select all True Statements""",
        'options': {'From the Azure portal, you can distinguish between services that are enerally available and services that are in public preview': True, 'After an Azure service service becomes generally available, the service is no longer updated with new features': None,
                    'When you create Azure resources for a service in the public preview, you must recreate the resources once the service becomes generally available': None},
        'explain_url': 'https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/',
        'explain': """https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/""",
        'notes': '',
        'history': '',
        # 'category': 'cost',
        'category': 'test',
        'q_type': 'multi',
        'id': 2229
        },
{'q': """Select all True Statements""",
        'options': {'When using an Azure ExpressRoute connection, inbound data traffic from an on-premises network to Azure is always free': True, 'Outbound data traffic from Azure to an on-premises network is always free': None,
                    'Data traffic between Azure services within the same Azure region is always free': True},
        'explain_url': 'https://azure.microsoft.com/en-us/pricing/details/expressroute/',
        'explain': """Box 1: Yes -
With Azure ExpressRoute, all inbound data transfer is free of charge.

Box 2: No -
Inbound data traffic is free but outbound data traffic is not.

Box 3: Yes -

https://azure.microsoft.com/en-us/pricing/details/expressroute/""",
        'notes': '',
        'history': '',
        # 'category': 'cost',
        'category': 'test',
        'q_type': 'multi',
        'id': 2230
        },

]


def create_table(filename=''):

    # conn = sqlite3.connect('questions.db')
    # conn = sqlite3.connect(tbl)
    conn = sqlite3.connect(f'{BASE_PATH}/{filename}')

    cmd = """CREATE TABLE tbl_questions
    (id INT PRIMARY KEY,
    q TEXT NOT NULL,
    options JSON NOT NULL,
    explain TEXT,
    explain_url TEXT,
    notes TEXT,
    history TEXT,
    category TEXT,
    q_type TEXT,
    misc TEXT,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);"""

    conn.execute(cmd)
    conn.close()


def add_to_sql(items, filename=''):

    # conn = sqlite3.connect('questions.db')
    conn = sqlite3.connect(filename)

    for itm in items:
        print(itm['id'])

        # explains = {'explain': itm.get('explain', ''),
        #             'explain_url': itm.get("explain_url", '')}

        cmd = 'Insert into tbl_questions (id, q, options, explain, explain_url, category, q_type) ' \
              'VALUES (?, ?, ?, ?, ?, ?, ?)'

        conn.execute(cmd, (int(itm["id"]), itm["q"], json.dumps(itm["options"]),
                           itm.get("explain"), itm["explain_url"],
                           itm.get("category", ""), itm["q_type"]))
        conn.commit()


def read_db(idx='', tmp_db=''):
    """ [ALL= 0 or ID]"""

    cmd = f'SELECT * from tbl_questions where id = {idx}'

    if idx == '0':
        cmd = 'SELECT * from tbl_questions'

    # conn = sqlite3.connect(f'{BASE_PATH}/questions.db')
    conn = sqlite3.connect(f'{BASE_PATH}/{tmp_db}')
    cursor = conn.execute(cmd)

    questions = []

    for row in cursor:
        idx, q, options, explain, explain_url, notes, history, category, q_type, misc, timestamp = row

        itm = {
            'id': idx,
            'q': q,
            'options': json.loads(options),
            'explain': explain,
            'explain_url': explain_url,
            'notes': notes,
            'history': history,
            'category': category,
            'q_type': q_type,
            'misc': misc,
            'timestamp': timestamp
        }
        questions.append(itm)

    return questions


def write_to_json_file(json_file='', ):
    """ Get questions, write to json file"""

    data = read_db(idx='0', tmp_db='questions.TMP.db')

    with open("questions.json", "w") as write_file:
        json.dump(data, write_file, indent=4)


def make_json_db(filename='', json_file='questions.json'):
    """ Read new json formatted file into mem, write into sqlite3 db"""

    # | Read sqlite3 items into json
    write_to_json_file(json_file)

    create_table(filename)

    # | Use json file to build sqlite db
    # f = open('questions.json')
    f = open(json_file)
    data = json.load(f)

    add_to_sql(data, filename=filename)


def main():

    # | Delete questions.db & questions.TMP.db
    if os.path.exists('questions.TMP.db'):
        os.remove('questions.TMP.db')

    if os.path.exists('questions.db'):
        os.remove('questions.db')

    # | Import raw questions into a new sqlite3 db
    create_table(filename='questions.TMP.db')
    # create_table(filename='questions.db')
    add_to_sql(items, filename='questions.TMP.db')
    # add_to_sql(items, filename='questions.db')

# | Step 2
    # | Export new db into a json file
    write_to_json_file(json_file='questions.json')

    # | Load json file into new questions.db
    create_table('questions.db')

    f = open('questions.json')
    data = json.load(f)

    add_to_sql(data, filename='questions.db')



main()


