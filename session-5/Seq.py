class Seq:
	def __init__(self,strbase):
		self.strbase=strbase
		def Class_initialization(self):
			pass
		def len(self):
			return len(self.strbase)
		def complement(self):
			complement_list = []
			for n in self.strbase:

				if n=="A":
					complement_list.append("T")
				elif n=="T":
					complement_list.append("A")
				elif n=="G":
					complement_list.append("C")
				elif n=="C":
					complement_list.append("G")
			return complement_list.strip(",")

		def reverse(self):
			reverse_list=[]
			n=len(self.strbase)-1
			while n>=0:
				reverse_list.append(self.strbase[n])
				n-=1
			return reverse_list.strip(",")


		def count(self, base):
			self.base=self.base.upper()
			return strbase.count(self.base)

		def perc(self, base):
			round(100.0 * strbase.count(base) / strbase.len , 1)

seq1=seq(“AGTC”)


