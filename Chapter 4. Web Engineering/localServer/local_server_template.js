const server = require('server')

const { get, post } = server.router

const getData = () => {
    console.log('someone asked for data')
    return new Promise((resolve, reject)=>{
        try {
            setTimeout(()=>{
                const products = [
                    {
                        name: 'phone',
                        price: 100,
                    },
                    {
                        name: 'headphone',
                        price: 200,
                    },
                    {
                        name: 'Kieran',
                        price: 300,
                    },
                ]
                console.log('success')
                resolve(products)
            })
        }
        catch (err) {
            console.log('ERROR')
            console.log(err)
            reject(err)
        }
    })
}

server(
    {port: 8000},  // first argument is an object of options
    [ // second argument is a list of routes
        get('/', ()=>{console.log('someone got "/"'); return 'Hello world'}) ,
        get('/data', ()=>{console.log('someone got "/data"'); return getData()}) ,
    ]
)