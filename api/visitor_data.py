
#For every station on Array Buffer to store the Hex values 

class Visitorflow():
      
    def get_data(self,data_swagger):
        
        self.data_swagger = data_swagger
        
        mac_buffer_1 = []
        wifi_counter_1 = []
        
        mac_buffer_2 = []
        wifi_counter_2 = []

        mac_buffer_3 = []
        wifi_counter_3 = []

        try: 
            for index in data_swagger:
                for item in index:
                    print("Item ",item)
                    if item == "device_id":

                        if index[item] == "messstation_1":
                            for mac_adr in index: 
                                if mac_adr == "macsBuffer": 
                                    if index[mac_adr] is None: 
                                        print("mac_adr is none")
                                    else:
                                        print("Macs Buffer = Data array is available")
                                        res_str = index[mac_adr][1:]
                                        rem_str = res_str[:-1]
                                        new_data = rem_str.split()
                                        print(new_data)
                                        for i in new_data:
                                            mac_buffer_1.append(i)
                                if mac_adr == "wifi":
                                    if index[mac_adr] is None:
                                        print("wifi is none")
                                    else:
                                        wifi_counter_1.append(index[mac_adr])
                                else:
                                    print("unrelevant")

                        if index[item] == "messstation_2":
                            for mac_adr in index: 
                                if mac_adr == "macsBuffer":
                                    if index[mac_adr] is None: 
                                        print("mac_adr is none")
                                    else:
                                        print("Macs Buffer = Data array is available")
                                        res_str = index[mac_adr][1:]
                                        rem_str = res_str[:-1]
                                        new_data = rem_str.split()
                                        print(new_data)
                                        for i in new_data:
                                            mac_buffer_2.append(i)
                                if mac_adr == "wifi":
                                    if index[mac_adr] is None:
                                        print("wifi is none")
                                    else: 
                                        wifi_counter_2.append(index[mac_adr])
                                else:
                                    print("unrelevant")

                        if index[item] == "messstation_3":
                            for mac_adr in index: 
                                if mac_adr == "macsBuffer":
                                    if index[mac_adr] is None: 
                                        print("mac_adr is none")
                                    else:
                                        print("Macs Buffer = Data array is available")
                                        res_str = index[mac_adr][1:]
                                        rem_str = res_str[:-1]
                                        new_data = rem_str.split()
                                        print(new_data)
                                        for i in new_data:
                                            mac_buffer_3.append(i)
                                if mac_adr == "wifi":
                                    if index[mac_adr] is None:
                                        print("wifi is none")
                                    else: 
                                        wifi_counter_3.append(index[mac_adr])
                                else:
                                    print("unrelevant")

                        elif item is None:
                            print("No validate Data in the Swagger") 
                    else:
                        pass
                        #print("Item key ", item)
                        #print("Index" , index)
                        #print("Value ", index[item])

        except Exception as e:
            return "Error",404
        
        print("MAC Buffer 1: ", mac_buffer_1) 
        print("Wifi Counter 1: ", wifi_counter_1) 
        
        print("Mac Buffer 2: ", mac_buffer_2) 
        print("Wifi Counter 2: ", wifi_counter_2) 

        print("Mac Buffer 3: ", mac_buffer_3) 
        print("Wifi Buffer 3: ", wifi_counter_3) 

        return [mac_buffer_1,wifi_counter_1,mac_buffer_2,wifi_counter_2,mac_buffer_3,wifi_counter_3]

    def work_with_wifi_data(self,wifi_counter_1,wifi_counter_2,wifi_counter_3):
        #calculate the average of the wifi counter 
        self.wifi_counter_1 = wifi_counter_1
        self.wifi_counter_2 = wifi_counter_2
        self.wifi_counter_3 = wifi_counter_3

        wifi_count = [wifi_counter_1,wifi_counter_2,wifi_counter_3]
        avg_result = [] 

        min_counter = 0 
        max_counter = 0 
        for i in wifi_count:
            len = 1
            avg_count =  0
            for counter in i: 
                avg_count = avg_count + counter 
                len += 1
                if counter >= max_counter:
                    max_counter = counter 
                else:
                    min_counter = counter 
            avg_count = avg_count / len 
            avg_result.append(avg_count)

        return [avg_result,max_counter,min_counter]


    def get_unique_list(self,mac_buffer):
        #create a array with unique mac adress in the lists 
        self.mac_buffer = mac_buffer

        unique_mac_storage  = []
        counter = 0

        for i in mac_buffer:
            if i not in unique_mac_storage:
                unique_mac_storage.append(i)
                counter += 1
            else:
                pass

        return [unique_mac_storage,counter]


    def compare_list_1_and_3(self,mac_buffer_1,mac_buffer_3):
        self.mac_buffer_1 = mac_buffer_1
        self.mac_buffer_3 = mac_buffer_3

        only_mss1 = [] 
        only_mss3 = []

        for i in mac_buffer_1:
            if i not in mac_buffer_3:
                only_mss1.append(i)
            else:
                pass 

        for i in mac_buffer_3: 
            if i not in mac_buffer_1:
                only_mss3.append(i)
            else:
                pass 

        return [only_mss1,only_mss3]

    def compare_lists_front(self,infront_list, inside_list ): 
        #mac adresses in front of bulding compare with inside MACs 
        self.infront_list = infront_list
        self.inside_list = inside_list

        inside = []
        counter = 0
        macs_not_allowed= []
        #only macs who are detected in front of building are allowed 
        for mac in inside_list: 
            if mac in infront_list:
                inside.append(mac)
                counter += 1
            else:
                macs_not_allowed.append(mac)
                
        #prozent berechenen die abgebogen sind 
        in_prc = 100 * (counter / len(infront_list)) 
        
        return [inside,counter,round(in_prc,2)]

    def compare_all_lists(self,mac_buffer_1,mac_buffer_2,mac_buffer_3):
        self.mac_buffer_1 = mac_buffer_1
        self.mac_buffer_2 = mac_buffer_2 
        self.mac_buffer_3 = mac_buffer_3 

        macs_not_allowed = []

        mac_inside = [] 
        counter = 0 
        
        for i in mac_buffer_2:
            if i in mac_buffer_1 or i in mac_buffer_3: 
                mac_inside.append(i)
                counter += 1
            else:
                macs_not_allowed.append(i)

        return [mac_inside,counter]


    def mac_data_front(self,mac_buffer_1,mac_buffer_2,mac_buffer_3):

        self.mac_buffer_1 = mac_buffer_1
        self.mac_buffer_2 = mac_buffer_2
        self.mac_buffer_3 = mac_buffer_3

        #counter how many diffrents macs in front of building and inside building
        analyze = Visitorflow()
        #infront of building Left
        in_front_L = analyze.get_unique_list(mac_buffer_1)
        #infront of building right
        in_front_R = analyze.get_unique_list(mac_buffer_3)
        #inside building
        inside_building = analyze.get_unique_list(mac_buffer_2)
        
        # no double MACs only from one pot mss1 + mss3 = in front complete data 
        get_unique_infront_list = analyze.get_unique_list(in_front_L[0]+in_front_R[0])
        # Expandable with more sensors in front of the building for more control  
        only_macs_mss2 = analyze.compare_lists_front(get_unique_infront_list[0],inside_building[0])
        
        #only MACs in Station 1 and 3 not MACs who are come from the opponent
        only_macs_mss1_3 = analyze.compare_list_1_and_3(in_front_L[0], in_front_R[0])


        return [in_front_L[1],in_front_R[1],only_macs_mss2[2],only_macs_mss1_3[0],only_macs_mss1_3[1] ]


    def mac_data_inside(self,mac_buffer_1,mac_buffer_2,mac_buffer_3):

        self.mac_buffer_1 = mac_buffer_1
        self.mac_buffer_2 = mac_buffer_2
        self.mac_buffer_3 = mac_buffer_3

        analyze = Visitorflow()

        #infront of building left
        in_front_L = analyze.get_unique_list(mac_buffer_1)
        #infront of building right
        in_front_R = analyze.get_unique_list(mac_buffer_3)
        #inside building
        inside_building = analyze.get_unique_list(mac_buffer_2)

        #man kann eigentlich nur in das gebäude kommen wenn man an station 1 oder 2 vorbeiläuft 
        result = analyze.compare_all_lists(in_front_L[0],inside_building[0],in_front_R[0])

        return [inside_building[1],result[0],result[1]]


    def mac_data_campus(self,mac_buffer_1,mac_buffer_2,mac_buffer_3):

        self.mac_buffer_1 = mac_buffer_1
        self.mac_buffer_2 = mac_buffer_2
        self.mac_buffer_3 = mac_buffer_3

        analyze = Visitorflow()

        #Campus Information
        #infront of building Left
        in_front_L = analyze.get_unique_list(mac_buffer_1)
        #infront of building right
        in_front_R = analyze.get_unique_list(mac_buffer_3)
        #inside building
        inside_building = analyze.get_unique_list(mac_buffer_2)

        #unique list from all 3 lists
        complete_unique_list = analyze.get_unique_list(in_front_L[0]+inside_building[0]+in_front_R[0])

        #get unique list counter number from list 1 and 3 in front of building 
        front_unique_list = analyze.get_unique_list(in_front_L[0]+in_front_R[0])

        return [complete_unique_list[1],front_unique_list[1],in_front_L[1],in_front_R[1]]
        

    def data_for_database(self,mac_buffer_1,mac_buffer_2,mac_buffer_3):
        self.mac_buffer_1 = mac_buffer_1
        self.mac_buffer_2 = mac_buffer_2
        self.mac_buffer_3 = mac_buffer_3

        analyze = Visitorflow()

        #Campus Information
        #infront of building Left
        in_front_L = analyze.get_unique_list(mac_buffer_1)
        #infront of building right
        in_front_R = analyze.get_unique_list(mac_buffer_3)
        #inside building
        inside_building = analyze.get_unique_list(mac_buffer_2)

        return [in_front_L[0],inside_building[0],in_front_R[0]]
