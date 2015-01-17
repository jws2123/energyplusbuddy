f = File.open("./Test_IDF.idf", "r")

i = 0
ary = []

f.each_line do |line|
  i += 1
  if line[0..7] == 'Material'
    ary[i] = 'm'
  elsif line[0..12] == 'Construction,'
    ary[i] = 'c'
  elsif line == "\r\n"
    ary[i] = 'b'
  elsif line[0] == ' '
    ary[i] = 'p'
  else
    ary[i] = 'x'
  end
end


#print "Constructions: "
cons =  ary.each_index.select{|j| ary[j] == 'c'}
#print "Materials: "
mats = ary.each_index.select{|j| ary[j] == 'm'}
#p ary.each_index.select{|j| ary[j] == 'p'}

fname = "Test_IDF.idf"

for k in 0..cons.length
  p File.readlines(fname)[cons[k]]
  mats.each do |m|
    if m < cons[k+1]
      print "\t"
      p File.readlines(fname)[m] 
    end
  end
  puts ""
end

f.close
