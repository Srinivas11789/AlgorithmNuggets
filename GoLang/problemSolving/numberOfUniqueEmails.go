func numUniqueEmails(emails []string) int {
    
    result := []string{}
    
    for _, email := range emails {
        
        // split local and domain name with "@"
        e := strings.Split(email, "@")
        localname, domainname := e[0], e[1]
        
        if strings.Contains(localname, ".") {
            localname = strings.Replace(localname, ".", "", -1)
        }
        
        if strings.Contains(localname, "+") {
            localname = strings.Split(localname, "+")[0]
        }
        
        // Debug
        //fmt.Println(localname+"@"+domainname)
        filtered_email := localname+"@"+domainname
        
        existence := 0
        for _, val := range result {
            if val == filtered_email {
                existence = 1
            }
        }
        
        if existence == 0 {
            result = append(result, filtered_email)
        }
        
    }
    
    return len(result)
}
