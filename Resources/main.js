// get a reference to a CSInterface object
var csInterface = new CSInterface();
var button = window.document.getElementById("btn");

button.onclick = function(){
	csInterface.evalScript("RunProductCodeGenerator()");	
};

