
print "hello world";
message = "hahahaha";
print message;
#--------------------------------------------------------------
# Python Var

int_var = 1;
long_var = 1000L;

info = "hello world";
print int_var;
print long_var;
print info[1:2];


#--------------------------------------------------------------
# List && Tuple
#--------------------------------------------------------------

print "===========================================================\n";
print "Data Type: List && Tuple\n";
print "===========================================================\n";

lstNum =  [1, 2, 3]
lstStr =  ["dota", "lol", "dota2"];
lstMisc = [lstNum, lstStr];

lstMisc.insert(0, "insertData");
lstMisc.append("appendData");
lstMisc.pop(1);

tupA = ('a', 'b', 'c');

#--------------------------------------------------------------
# Dict
#--------------------------------------------------------------
print "===========================================================\n";
print "Data Type: Dict\n";
print "===========================================================\n";

dictA = {"lahm" : "Bayern", "phil" : "UESTC"};

print dictA{"phil"} + "\n";
print dictA.values() + "\n";
print dictA.items()  + "\n";






