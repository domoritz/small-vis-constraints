import {TopLevelSpec} from 'vega-lite';

export function asp2vl(asp: any): TopLevelSpec[] {
    let specs: TopLevelSpec[] = [];

    const witnesses = getWitnesses(asp);
    if (witnesses) {
        specs = witnesses.map((witness: any) => {
            let mark = '';
            let encoding = {scale: {}};

            witness.Value.forEach((value: string) => {
                const valueType = value.split('(')[0];
                switch(valueType) {
                    case 'mark':
                        mark = value.replace('mark(', '').replace(')', '');
                        break;
                    
                    case 'field':
                    case 'channel':
                    case 'type':
                    case 'zero':

                    default:
                        break;

                }
            });

            return {
                '$schema': 'https://vega.github.io/schema/vega-lite/v2.0.json',
                data: {url: 'data/cars.json'},
                mark,
                encoding
            };
        });
    }
    console.log('specs', specs);
    return specs;
}

/** 
 * Get the array of witnesses from clingo output. 
 * Return undefined if no witnesses were found. 
 */
function getWitnesses(asp: any) {
    const result = JSON.parse(asp);

    if(result.Call && result.Call.length > 0) {
        return result.Call[0].Witnesses;
    } else {
        return undefined;
    }
}
