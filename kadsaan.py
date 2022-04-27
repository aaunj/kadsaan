from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<string:name>')

def kadsaanfn(name):
    nameList = ['ศศิกานต์ ขำปลื้มจิตร์',
                'ไอรดา บุญมาวงค์',
                'วรัตนาพร อินทนา',
                'ณัฐวรา วัชรธรรม',
                'กริ่มกมล ถาวร',
                'ทศพร สอนโต',
                'สราวุฒิ มาสรวง',
                'สุภาภรณ์ สีเขียว',
                'ทิพวรรณ ทองล้น',
                'สายชล จันทร์หา',
                'พรพรรณ ใจวงค์',
                'อมรเทพ สืบสาย',
                'อภิชาติ นันทารัมภ์',
                'ภาณุวิชญ์ ปานพวงแก้ว',
                'อภิกา อนุอัน',
                'ณัฏฐินันท์ กฤษสุริยา',
                'ทัศนีย์ คนหาญ',
                'นภัทร จินดากุล',
                'สิริการย์ ธนกุลศรีโรจน์',
                'ธันยากร ครองยุติ',
                'วิชุดา ทองทวี',
                'วริญา นาลัย',
                'รสสุริน ชินอ่อน',
                'ธนวัฒน์ ยงประเดิม',
                'อรุณชัย อภิชาติวรนันท์',
                'ณัฐชญา มีมานะ',
                'พัชรี ง้าวไข่น้ำ',
                'ปุณณดา ใจมูล',
                'จันธิมา มีงาน',
                'นิตยา กุณธิ',
                'มณฑิรา เข็มรัตน์',
                'จงรัก ภู่ระหงษ์',
                'ทัศนีย์ สมประสงค์',
                'วรุณ เปลี่ยนแสง',
                'จุรี มาชาวนา',
                'ภัทรานิษฐ์ พึ่งพิง',
                'ธมลพรรณ พลจันทร์',
                'พชรพรพรรณ สอนหาจักร',
                'ณัชชา นาคจตุรานนท์',
                'รัชต์รวีย์ จักษุสุวรรณ',
                'เขมจิรา กล่องแก้ว',
                'มณฑาทิพย์ ท้อสุวรรณ',
                'พนารัตน์ ภุมรินทร์',
                'เมลดา จาติกานนท์',
                'ชาติมงคล วงค์มา',
                'ณัฐชนก ตันฑเตมีย์',
                'สุภาวดี รัตนวิเศษ',
                'ไชยวัฒน์ นิติพุฒิพร',
                'นันทพร จระมาศ',
                'ภิญญาพัชญ์ เขียวทองอินทร']

    house = ['กริฟฟินดอร์', 'ฮัฟเฟิลพัฟ', 'เรเวนคลอ', 'สลิธีรีน']

    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    names = []

    for name in nameList:
        num = len(name.replace(" ", "")) % 4

        ##house = ['กริฟฟินดอร์','ฮัฟเฟิลพัฟ','เรเวนคลอ','สลิธีรีน']
        ## กริฟฟินดอร์ -> สลิธีรีน -> ฮัฟเฟิลพัฟ -> เรเวนคลอ
        if num == 0:
            if len(gryffindor) == 13:
                if len(slytherin) < 13:
                    house = 'สลิธีรีน'
                    slytherin.append(name)
                elif len(hufflepuff) < 13:
                    house = 'ฮัฟเฟิลพัฟ'
                    hufflepuff.append(name)
                else:
                    house = 'เรเวนคลอ'
                    ravenclaw.append(name)
            else:
                house = 'กริฟฟินดอร์'
                gryffindor.append(name)


        ##house = ['กริฟฟินดอร์','ฮัฟเฟิลพัฟ','เรเวนคลอ','สลิธีรีน']
        ## ฮัฟเฟิลพัฟ  -> เรเวนคลอ -> กริฟฟินดอร์ -> สลิธีรีน
        elif num == 1:
            if len(hufflepuff) == 13:
                if len(ravenclaw) < 13:
                    house = 'เรเวนคลอ'
                    ravenclaw.append(name)
                elif len(gryffindor) < 13:
                    house = 'กริฟฟินดอร์'
                    gryffindor.append(name)
                else:
                    house = 'สลิธีรีน'
                    slytherin.append(name)
            else:
                house = 'ฮัฟเฟิลพัฟ'
                hufflepuff.append(name)

        ##house = ['กริฟฟินดอร์','ฮัฟเฟิลพัฟ','เรเวนคลอ','สลิธีรีน']
        ## เรเวนคลอ  -> กริฟฟินดอร์ -> ฮัฟเฟิลพัฟ -> สลิธีรีน
        elif num == 2:
            if len(ravenclaw) == 13:
                if len(gryffindor) < 13:
                    house = 'กริฟฟินดอร์'
                    gryffindor.append(name)
                elif len(hufflepuff) < 13:
                    house = 'ฮัฟเฟิลพัฟ'
                    hufflepuff.append(name)
                else:
                    house = 'สลิธีรีน'
                    slytherin.append(name)
            else:
                house = 'เรเวนคลอ'
                ravenclaw.append(name)


        ##house = ['กริฟฟินดอร์','ฮัฟเฟิลพัฟ','เรเวนคลอ','สลิธีรีน']
        ## สลิธีรีน  -> ฮัฟเฟิลพัฟ -> เรเวนคลอ -> กริฟฟินดอร์
        else:
            if len(slytherin) == 13:
                if len(hufflepuff) < 13:
                    house = 'ฮัฟเฟิลพัฟ'
                    hufflepuff.append(name)
                elif len(ravenclaw) < 13:
                    house = 'เรเวนคลอ'
                    ravenclaw.append(name)
                else:
                    house = 'กริฟฟินดอร์'
                    gryffindor.append(name)
            else:
                house = 'สลิธีรีน'
                slytherin.append(name)

        names.append('{} อยู่บ้าน {}'.format(name, house))

    return render_template('myTemplate.html', name1=names[0]
                           ,name2=names[1]
                           , name3=names[2]
                           , name4=names[3]
                           , name5=names[4]
                           , name6=names[5]
                           , name7=names[6]
                           , name8=names[7]
                           , name9=names[8]
                           , name10=names[9]
                           , name11=names[10]
                           , name12=names[11]
                           , name13=names[12]
                           , name14=names[13]
                           , name15=names[14]
                           , name16=names[15]
                           , name17=names[16]
                           , name18=names[17]
                           , name19=names[18]
                           , name20=names[19]
                           , name21=names[20]
                           , name22=names[21]
                           , name23=names[22]
                           , name24=names[23]
                           , name25=names[24]
                           , name26=names[25]
                           , name27=names[26]
                           , name28=names[27]
                           , name29=names[28]
                           , name30=names[29]
                           , name31=names[30]
                           , name32=names[31]
                           , name33=names[32]
                           , name34=names[33]
                           , name35=names[34]
                           , name36=names[35]
                           , name37=names[36]
                           , name38=names[37]
                           , name39=names[38]
                           , name40=names[39]
                           , name41=names[40]
                           , name42=names[41]
                           , name43=names[42]
                           , name44=names[43]
                           , name45=names[44]
                           , name46=names[45]
                           , name47=names[46]
                           , name48=names[47]
                           , name49=names[48]
                           , name50=names[49]
                           ,gryffindorcount=len(gryffindor)
                           ,hufflepuffcount=len(hufflepuff)
                           ,ravenclawcount=len(ravenclaw)
                           ,slytherincount=len(slytherin))



def Home(name):
  return render_template('myTemplate.html')

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)




