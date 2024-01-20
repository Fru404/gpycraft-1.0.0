from gpycraft.fileIO.filecraft import filecraft
import pandas as pd
io=filecraft()

#print(io.read_dotfile('asdotfile..'))

#df=io.read_dotfile('new..')

#print(io.write_dotfile(df))
#cols=['Units Sold','Sale Price','Gros Sales','Profit']
#io.in_dotfile('Financial Sample.xlsx','asdotfile..',column=cols)



#data=io.dotfile_aspd('new.txt')
#print(data.columns)
#coladd=['Semester']
#print(io.xl_asdotfile(xl_filePath='output_data.xlsx',dotfile_path='collage.txt',column=coladd))
#coladd=['Semester']
io.dotfile_asxl('new.txt',fieldNumber=4,byPass=True)