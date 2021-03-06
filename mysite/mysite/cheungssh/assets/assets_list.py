#!/usr/bin/env python
#coding:utf-8

assets_conf={
				"disk_number":{
							"name":"硬盘(个)",
							"command":{
									"CentOS/RedHat5":"""mount -l|grep -Eo '^/dev/[a-zA-Z]+'|sort|uniq|wc -l""",
									"CentOS/RedHat6":"""mount -l|grep -Eo '^/dev/[a-zA-Z]+'|sort|uniq|wc -l""",
									"CentOS/RedHat7":"""mount -l|grep -Eo '^/dev/[a-zA-Z]+'|sort|uniq|wc -l""",
									"Ubuntu":"""mount -l|grep -Eo '^/dev/[a-zA-Z]+'|sort|uniq|wc -l""",
									"Aix":"""mount |grep   '/dev/'|sort|uniq|wc -l""",
									"Solaris":"""mount -l|grep -Eo '^/dev/[a-zA-Z]+'|sort|uniq|wc -l""",
								},
							"type":"number",
							"show":True,
						},
				"system_version":{
							"name":"系统版本",
							"command":{
								"CentOS/RedHat5":"""echo  'import platform;print platform.dist()[1]'|python""",
								"CentOS/RedHat6":"""echo  'import platform;print platform.dist()[1]'|python""",
								"CentOS/RedHat7":"""echo  'import platform;print platform.dist()[1]'|python""",
								"Ubuntu":"""echo  'import platform;print platform.dist()[1]'|python""",
								"Aix":"""uname -a""",
								"Solaris":""" """,
							},
							"type":"number",
							"show":True,
					},
				"system_user":{
							"name":"账号清单",
							#"command":"""awk  -F ':' '{print $1}' /etc/passwd""",
							"command":{
								"CentOS/RedHat5":"""awk  -F ':' '{print $1}' /etc/passwd""",
								"CentOS/RedHat6":"""awk  -F ':' '{print $1}' /etc/passwd""",
								"CentOS/RedHat7":"""awk  -F ':' '{print $1}' /etc/passwd""",
								"Ubuntu":"""awk  -F ':' '{print $1}' /etc/passwd""",
								"Aix":"""awk  -F ':' '{print $1}' /etc/passwd""",
								"Solaris":"""awk  -F ':' '{print $1}' /etc/passwd""",
							},
							"type":"string",
							"show":True,
					},
				"disk_mount":{
							"name":"挂载点",
							"command":{
								"CentOS/RedHat5":"""mount|egrep  '^ */'""",
								"CentOS/RedHat6":"""mount|egrep  '^ */'""",
								"CentOS/RedHat7":"""mount|egrep  '^ */'""",
								"Ubuntu":"""mount|egrep  '^ */'""",
								"Aix":"""mount|egrep  '^ */'""",
								"Solaris":"""mount|egrep  '^ */'""",
							},
							"type":"string",
							"show":True,	
					},
				"logic_cpu_number":{
						"name":"CPU(个)",
						"command":{
							"CentOS/RedHat5":"""grep "processor"  /proc/cpuinfo| wc -l""",
							"CentOS/RedHat6":"""grep "processor"  /proc/cpuinfo| wc -l""",
							"CentOS/RedHat7":"""grep "processor"  /proc/cpuinfo| wc -l""",
							"Ubuntu":"""grep "processor"  /proc/cpuinfo| wc -l""",
							"Aix":"""pmcycles -m|wc -l""",
							"Solaris":"""grep "processor"  /proc/cpuinfo| wc -l""",
						},
						"type":"number",
						"show":True,
					},
				"cpu_core":{
					"name":"CPU(核)",
					"command":{
						"CentOS/RedHat5":"""grep "core id" /proc/cpuinfo |sort|uniq|wc -l""",
						"CentOS/RedHat6":"""grep "core id" /proc/cpuinfo |sort|uniq|wc -l""",
						"CentOS/RedHat7":"""grep "core id" /proc/cpuinfo |sort|uniq|wc -l""",
						"Ubuntu":"""grep "core id" /proc/cpuinfo |sort|uniq|wc -l""",
						"Aix":"""prtconf|grep Processors |awk  '{print $NF}'""",
						"Solaris":"""grep "core id" /proc/cpuinfo |sort|uniq|wc -l""",
					},
					"type":"number",
					"show":True,
				},
				"sn":{
					"name":"序列号",
					"command":{
						"CentOS/RedHat5":"""/usr/sbin/dmidecode  -s system-serial-number""",
						"CentOS/RedHat6":"""/usr/sbin/dmidecode  -s system-serial-number""",
						"CentOS/RedHat7":"""/usr/sbin/dmidecode  -s system-serial-number""",
						"Ubuntu":"""/usr/sbin/dmidecode  -s system-serial-number""",
						"Aix":"""prtconf | grep "Machine Serial Number"|awk '{print $NF}'""",
						"Solaris":""" """,
					},
					"type":"string",
					"show":True,
				},
				"run_time":{
					"name":"运行时间",
					"command":{
						"CentOS/RedHat5":"""uptime|awk  -F 'user|up' '{print $2}'|awk -F ',' '{print $1 $2}'""",
						"CentOS/RedHat6":"""uptime|awk  -F 'user|up' '{print $2}'|awk -F ',' '{print $1 $2}'""",
						"CentOS/RedHat7":"""uptime|awk  -F 'user|up' '{print $2}'|awk -F ',' '{print $1 $2}'""",
						"Ubuntu":"""uptime|awk  -F 'user|up' '{print $2}'|awk -F ',' '{print $1 $2}'""",
						"Aix":"""uptime|awk  -F 'user|up' '{print $2}'|awk -F ',' '{print $1 $2}'""",
						"Solaris":"""uptime|awk  -F 'user|up' '{print $2}'|awk -F ',' '{print $1 $2}'""",
					},
					"type":"string",
					"show":True,
				},
				"IP":{
					"name":"IP",
					"command":{
						"CentOS/RedHat5":"""ifconfig|grep -Po '(?<=addr:).*(?=  Bcast)'""",
						"CentOS/RedHat6":"""ifconfig|grep -Po '(?<=addr:).*(?=  Bcast)'""",
						"CentOS/RedHat7":"""ifconfig|grep -Po '(?<=addr:).*(?=  Bcast)'""",
						"Ubuntu":"""ifconfig|grep -Po '(?<=addr:).*(?=  Bcast)'""",
						"Aix":"""ifconfig  -a|grep inet|awk '{print $2}'|egrep  '^[0-9]'|grep  -v '127.0.0.1'""",
						"Solaris":""" """,
					},
					"type":"string",
					"show":True,
				},
}
	
