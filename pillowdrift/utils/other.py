import sys    


def startapp(configpath, datapath_ref, datapath_cur, datapath_system):
    pass

def stopapp():
    pass

def pillowdrift(options=sys.argv[1:]):

    if "start" in options:
        options_dict = {}
        for element_value in options:
            if element_value != "start":
                element, value = element_value.split("=")
                element, value = element.strip(), value.strip()
                options_dict[element] = value
        options_count = 0
        if "--configpath" not in options_dict.keys():
            print("Enter the config path !")
        else:
            options_count += 1
        if "--datapath-ref" not in options_dict.keys():
            print("Enter the reference data path !")
        else:
            options_count += 1
        if "--datapath-cur" not in options_dict.keys():
            print("Enter the current data path !")
        else:
            options_count += 1
        if "--datapath-system" not in options_dict.keys():
            print("Enter the service data path !")
        else:
            options_count += 1
            
        
        if options_count == 4:
            configpath = options_dict["--configpath"]
            datapath_ref = options_dict["--datapath-ref"]
            datapath_cur = options_dict["--datapath-cur"]
            datapath_system = options_dict["--datapath-system"]
            # Start flask server
            print("Lancement de l'application ...\n")
            print("les configurations sont: ", options_dict)
            startapp(configpath, datapath_ref, datapath_cur, datapath_system)
    elif "stop" in options:
        # Stop flask server
        pass
    else:
        print("Provide one action: start or stop !")
        
    pass

