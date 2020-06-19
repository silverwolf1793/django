class Paginator{
    constructor(range,activeNumber,displayNumberLimit,paginatorId){
        if (
            range == undefined ||
            activeNumber == undefined ||
            displayNumberLimit == undefined ||
            paginatorId == undefined 
        )
            throw Error("Wrong arguments!")
        this.active = activeNumber
        this.displayNumberLimit = displayNumberLimit
        this.divAnchor = document.getElementById(paginatorId) 
        this.divAnchor.innerHTML = ""
        this.divAnchor.classList.add("paginator")
        this.range = this.rangeStringToArray(range)
    }
    
    rangeStringToArray (range){
        let buffer = range.replace("range(","").replace(")","")
        let result = buffer.split(',')
        return [parseInt(result[0]), parseInt(result[1])]
    }

    load(){
        this.divAnchor.innerHTML += "<div class='arrow left'></div>"
        if (this.range[1] <= this.displayNumberLimit){            
            for(let i = this.range[0]; i<= this.range[1] -1; i++){
                if (i != this.active)
                    this.divAnchor.innerHTML += "<a href='./?page="+i+"' class='btn btn-secondary'>"+i+"</a>"
                else
                    this.divAnchor.innerHTML += "<div class='active'>"+i+"</div>"
            }
        }
        this.divAnchor.innerHTML += "<div class='arrow right'></div>"
    }
} 
