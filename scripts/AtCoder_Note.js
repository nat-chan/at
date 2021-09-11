let find_elements = function(xpath){
    let results = document.evaluate(
        xpath,
        document,
        null,
        XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
        null
    );
    return results;
};

let map_elements = function(f, xpaths){
    xpaths.forEach(xpath =>{
        let elements = find_elements(xpath);
        for(let i=0; i<elements.snapshotLength; i++){
            f(elements.snapshotItem(i));
        }
    });
};

let grid_sheet = function(unit, width, height){
    let table = '';
    table += '<table border frame=void style="border-color:rgba(202,235,253,0.7);table-layout:fixed;">';
    table += (`<tr height=${unit}>`+`<td width=${unit}></td>`.repeat(width)+`</tr>`).repeat(height);
    table += '</table>';
    return table;
};

let main = function(){
    map_elements(
        element => {
            element.remove();
        },
        [
            '//div[@class="div-btn-copy"]',
            '//a[@class="btn btn-default btn-sm"]',
            '//span[@id="task-lang-btn"]',
            '//span[@class="btn btn-default btn-sm btn-copy"]',
            '//hr',
            '//div[@class="alert alert-warning alert-dismissible fade in"]',
            '//form[@class="form-horizontal form-code-submit"]',
            '//div[@class="col-sm-12"]/span[@class=""]',
        ]
    );
    map_elements(
        element => {element.style = "display: inline-block;overflow-x:hidden;";},
        ['//pre']
    );
    map_elements(
        element => {
            let title = element.innerHTML.split(" - ").slice(1)[0];
            let problem_id = location.href.split("/").slice(-1)[0];
            element.innerHTML = `${problem_id.toUpperCase()} ${title}`;
            document.title = problem_id;
        },
        ['//span[@class="h2"]']
    );
    let root_element = find_elements('//div[@class="col-sm-12"]').snapshotItem(0);
    //root_element.innerHTML = root_element.innerHTML.replaceAll('。', '。<br>').replaceAll('、', '、<wbr>')
    let root_height = root_element.scrollHeight;
    //let pdf_height = 1028; //縦A4
    //let ratio = 0.7; //縦A4
    //let ratio = 1.6; //横Tabloid
    //let ratio = 1.5; //横Tabloid
    //let pdf_height = 960; //横Tabloid
    //let unit = 34; //横Tabloid
    let ratio = 1.4; //横A0
    let pdf_height = 2700; //横A0
    let unit = 30; //横A0
    let zoom = pdf_height/root_height;
    let height = root_height/unit;
    let width = height*ratio;
    height = Math.floor(height);
    width = Math.floor(width)/4; // TODO /5
    let grid = grid_sheet(unit, width, height);
    document.body.innerHTML = `
    <div style='position:relative;zoom:${zoom};'>
        <div style='position:absolute;'>
            ${grid}
        </div>
        <div style='position:absolute;width:600px;'>
            ${root_element.innerHTML}
        </div>
    </div>`
    print();
};
main();
location.reload();