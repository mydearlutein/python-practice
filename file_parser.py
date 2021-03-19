import argparse
import os
import datetime
import json


LOG_FILE = "result_{}.log".format(datetime.datetime.now().strftime("%Y%m%d"))


def write_log(log_file_name,log,printable=True):
    with open(log_file_name,"a+",encoding="utf-8") as f:
        f.write(log+"\n")
    if printable:
        print(log)


def extract_from_pdfminer_by_page(file_dir,file,target_format):
    from io import StringIO
    from pdfminer.converter import HTMLConverter,TextConverter
    from pdfminer.pdfinterp import PDFPageInterpreter
    from pdfminer.pdfinterp import PDFResourceManager
    from pdfminer.pdfpage import PDFPage

    with open(os.path.join(file_dir,file),"rb") as f:
        for page in PDFPage.get_pages(f,
                caching=True,
                check_extractable=True):
            resource_manager=PDFResourceManager()
            fake_file_handle=StringIO()
            _converter=HTMLConverter if target_format=="html" else TextConverter
            converter=_converter(resource_manager,fake_file_handle)
            page_interpreter=PDFPageInterpreter(resource_manager,converter)
            page_interpreter.process_page(page)

            text=fake_file_handle.getvalue()
            yieldtext

            #closeopenhandles
            converter.close()
            fake_file_handle.close()


def extract_from_mammoth(source_dir,file,target_format):

    import mammoth
    with open(os.path.join(source_dir,file),'rb') as f:
        if target_format=="html":
            document=mammoth.convert_to_html(f)
        else:
            document=mammoth.extract_raw_text(f)
        text=document.value
    #print(text)
    return[text]


def extract_from_hwp(source_dir,file,target_format):
    return[]


def extract_data(source_dir,file_groups,target_format):

    new_dir=os.path.join(source_dir,"convert")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    for format_type,files in file_groups.items():
        _separated=True if format_type=="pdf" else False
        extractor=extract_from_pdfminer_by_page if format_type=="pdf"\
            else extract_from_mammoth if format_type=="docx" else extract_from_hwp

        for file_name in files:
            data={'file_name':"",'source_format':format_type,'target_format':target_format,
            'page_separated':_separated,'pages':[],'context':""}

            for i,page in enumerate(extractor(source_dir,file_name,target_format)):
                if not page:
                    continue
                data['pages'].append({'page_num':i+1,'context':page})
                data['context']+=page

            new_file_name="{}_convert_{}.json".format(target_format,"".join(file_name.split(".")[:-1]))
            print(new_file_name)

            with open(os.path.join(new_dir,new_file_name),"w",encoding="utf-8") as new_f:
                json.dump(data,new_f,ensure_ascii=False)

            if target_format=="html" and data['context']:
                with open(os.path.join(new_dir,
                        "({}){}.html".format(format_type,"".join(file_name.split(".")[:-1]))),
                        "w",encoding="utf-8")asf:
                    f.write(data['context'])


if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Fileparsertest')
    parser.add_argument('--source_format',help='Sourcefileformat(pdf,docx,hwp)',required=False,default="")
    parser.add_argument('--source_dir',help='Targetfiledirectory')
    parser.add_argument('--target_format',help='TargetFileformat(text,html)')
    parser.add_argument('--log_file',help='Logfilefullpath',required=False,default="")
    args=parser.parse_args()

    source_dir=args.source_dir
    source_format=args.source_format
    target_format=args.target_format
    log_file=source_dir+args.log_fileifargs.log_fileelseLOG_FILE

    write_log(log_file,"+----------------------------------------------------+")
    write_log(log_file,"{}{}{}{}".format(str(__file__),source_format,source_dir,log_file))

    file_names=os.listdir(source_dir)
    file_groups={"pdf":[],"docx":[],"hwp":[]}
    for file in file_names:
        if file.split(".")[-1]=="pdf":
            file_groups["pdf"].append(file)
        elif file.split(".")[-1]=="docx":
            file_groups["docx"].append(file)
        elif file.split(".")[-1]=="hwp":
            file_groups["hwp"].append(file)
        else:
            continue

    print(file_groups)
    print(["{}:{}".format(k,len(v)) for k,v in file_groups.items()])

    extract_data(source_dir,file_groups,target_format)
