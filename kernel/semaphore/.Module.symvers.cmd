cmd_/home/doogunwo/Desktop/Computer-Science/kernel/semaphore/Module.symvers := sed 's/\.ko$$/\.o/' /home/doogunwo/Desktop/Computer-Science/kernel/semaphore/modules.order | scripts/mod/modpost -m -a  -o /home/doogunwo/Desktop/Computer-Science/kernel/semaphore/Module.symvers -e -i Module.symvers   -T -