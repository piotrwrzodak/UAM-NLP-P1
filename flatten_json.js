
// save json file
function downloadObjectAsJson(exportObj, exportName){
    var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportObj));
    var downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href",     dataStr);
    downloadAnchorNode.setAttribute("download", exportName + ".json");
    document.body.appendChild(downloadAnchorNode); // required for firefox
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
  }


// current exchange rates
const gbp_to_pln = 5.44
const chf_to_pln = 4.35
const eur_to_pln = 4.55
const usd_to_pln = 4.00


const calculateSalary = (currency, mean) => {
    switch(currency){
        case 'pln': return mean
        case 'gbp': return mean * gbp_to_pln
        case 'eur': return mean * eur_to_pln
        case 'usd': return mean * usd_to_pln
        case 'chf': return mean * chf_to_pln
        default: return 0
    }
}


const flattenJson = (data) => {
  return data.map(({
        employment_types,
         skills, ...rest}) => {
            const {from, to, currency} = employment_types[0].salary
            const type = employment_types[0].type
            const mean = (from + to) / 2
            let x =  {
                type: type,
                salary: calculateSalary(currency, mean),
                ...rest
            }

            skillList = skills.reduce(
                (obj, item, index) => Object.assign(obj, { [`skill`.concat(index)]: item.name, [`level`.concat(index)]: item.level }), {});

            return Object.assign(x, skillList)
  })
}

//downloadObjectAsJson(flattenJson(data), "flattened")
