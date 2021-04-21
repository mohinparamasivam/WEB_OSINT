import argparse
import sys
import os
import time

parser = argparse.ArgumentParser(description='WEB OSINT')
parser.add_argument('-d',help='Domain Name')
args = parser.parse_args()
domain = args.d


if len(sys.argv)==1:
	parser.print_help()
	sys.exit(1)

print("\n")	
print ("                                                                       ")
print ("                                                                       ")
print ("            ##########################################################" )       
print ("            #                                                        #" )        
print ("            #              	    WEB OSINT             	     #" ) 
print ("            #                                                        #" )                            
print ("            #         Author : Mohin Paramasivam   (Shad0wQu35t)     #" )       
print ("            #                                                        #" )       
print ("            ##########################################################" )    

print("\n")
print("\033[1;34;40m  Installing Dependencies \033[0m ")
print("\n")

os.system("apt-get update")
os.system("apt install subfinder")
print(" \033[1;34;40m subfinder Installed \033[0m ")
time.sleep(1)

os.system("apt install sublist3r")
print(" \033[1;34;40m sublist3r Installed \033[0m ")
time.sleep(1)

os.system("apt install eyewitness")
print(" \033[1;34;40m  EyeWitness Installed \033[0m ")
time.sleep(1)


print("\n")

time.sleep(1)

print(" \033[1;34;40m Running Subfinder against %s \033[0m " %(domain))

time.sleep(1)


domain_output_dir = domain.split('.')[0]
os.system("mkdir OSINT_RESULTS/")
os.system("rm  OSINT_RESULTS/%s" %(domain_output_dir))
os.system("mkdir OSINT_RESULTS/%s" %(domain_output_dir))
os.system("mkdir OSINT_RESULTS/%s/subdomains_result/" %(domain_output_dir))
time.sleep(3)

print('\n')
print("\033[1;34;40m Command : subfinder -d %s -oD OSINT_RESULTS/%s/subdomains_result -o subfinder_results.txt -oI -nW \033[0m " %(domain,domain_output_dir))
subfinder_command = "subfinder -d %s -o OSINT_RESULTS/%s/subdomains_result/subfinder_results.txt -oI -nW" %(domain,domain_output_dir)
os.system(subfinder_command)
print("\n")
time.sleep(1)
print("\033[1;34;40m Subfinder Complete! \033[0m ")

print("\n")

print("\033[1;34;40m Running Sublist3r against %s \033[0m " %(domain))
time.sleep(1)

print("\n")

print(" \033[1;34;40m Command : sublist3r -d %s -o OSINT_RESULTS/%s/subdomains_result/sublist3r_results.txt \033[0m " %(domain,domain_output_dir))
sublist3r_command = "sublist3r -d %s -o OSINT_RESULTS/%s/subdomains_result/sublist3r_results.txt" %(domain,domain_output_dir)

os.system(sublist3r_command)

time.sleep(1)
print("\n")

print("\033[1;34;40m Sublist3r Complete! \033[0m ")

print("\n")

print("\033[1;34;40m Compiling Domains into hosts.txt \033[0m ")
time.sleep(1)

os.system("touch OSINT_RESULTS/%s/subdomains_result/hosts.txt" %(domain_output_dir))

hosts_file_path = "OSINT_RESULTS/%s/subdomains_result/hosts.txt" %(domain_output_dir)
hosts_file_write = open(hosts_file_path,"w")


subfinder_raw_output_path = "OSINT_RESULTS/%s/subdomains_result/subfinder_results.txt" %(domain_output_dir)

os.system("cat %s | cut -d ',' -f 1 > OSINT_RESULTS/%s/subdomains_result/subfinder_hosts.txt" %(subfinder_raw_output_path,domain_output_dir))

subfinder_output_hosts = "OSINT_RESULTS/%s/subdomains_result/subfinder_hosts.txt" %(domain_output_dir)
subfinder_output_file = open(subfinder_output_hosts,"r").read()

sublist3r_output_path = "OSINT_RESULTS/%s/subdomains_result/sublist3r_results.txt" %(domain_output_dir)
sublist3r_output_file = open(sublist3r_output_path,"r").read()


#write subfinder output and append sublister output
print("\n")
print("\033[1;34;40m Writing Subfinder Results \033[0m ")
print("\n")



hosts_file_write.write(subfinder_output_file)
hosts_file_write.close()

hosts_file_append = open(hosts_file_path,"a")

print("\033[1;34;40m Writing Sublist3r Results \033[0m ")
print("\n")

hosts_file_append.write(sublist3r_output_file)
hosts_file_append.close()


print("\033[1;34;40m Domains Written to OSINT_RESULTS/%s/subdomains_result/hosts.txt \033[0m " %(domain_output_dir))
time.sleep(1)

print("\n")

print("\033[1;34;40m Running Eyewitness against Domains \033[0m ")
time.sleep(1)


os.system("mkdir OSINT_RESULTS/%s/eyewitness_results/" %(domain_output_dir))

os.system("eyewitness -f OSINT_RESULTS/%s/subdomains_result/hosts.txt -d OSINT_RESULTS/%s/eyewitness_results/ --prepend-https --timeout 10 --no-prompt" %(domain_output_dir,domain_output_dir))


time.sleep(1)

print("\n")

print("\033[1;34;40m Eyewitness Complete! \033[0m ")

print("\n")

print("\033[1;34;40m Running NMAP Scan \033[0m ")
time.sleep(1)

print("\n")

os.system("mkdir OSINT_RESULTS/%s/nmap_results/" %(domain_output_dir))

hosts_read_path = "OSINT_RESULTS/%s/subdomains_result/hosts.txt" %(domain_output_dir)

hosts_file_read = open(hosts_read_path,"r").read().splitlines()

for host in hosts_file_read:
	print("\033[1;34;40m Running NMAP on %s \033[0m " %(host))
	nmap_command = "nmap %s -vv -T3 -oN OSINT_RESULTS/%s/nmap_results/%s.nmap" %(host,domain_output_dir,host)
	os.system(nmap_command)
	print("\n")
	

print("\033[1;34;40m TASK COMPLETED! \033[0m ")

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
