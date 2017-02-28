def is_merge(s, part1, part2):
    if not part1:
      print "s1"
      return s == part2
      
    if not part2:
      print "s2"
      return s == part1
    if not s:
      print "s3"
      return part1 + part2 == ''
    print s,part1,part2
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
      print s
      return True
    
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
      
      return True
      
    
    return False

    #if s4== list(s):
     #   return True
    #else:
     #   return 
        

print is_merge('keshav', 'ksa', 'ehv')