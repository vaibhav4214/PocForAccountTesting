
import { useEffect, useState,  } from 'react';
import './App.css';

function App() {

            let getAccountNumber=window.location.pathname.slice(1)
            const data=[{accNo:1456325698,Name:"Vaibhava",Balance:"$1400.50",Status:"Not Ok"}
              ,{accNo:9698569658,Name:"Rahul",Balance:"$1300.50",Status:"Ok"},
              {accNo:9695696965,Name:"Rahul",Balance:"$1300.50",Status:"Ok"}

            ]
            const useraccNo=parseInt(getAccountNumber)
            let [details,setDetails]=useState({})
            
              useEffect(()=>
              {
                getAccData(useraccNo)
              },[])

              const getAccData=async(useraccNo)=>
              {
                    data.map((e)=>
                    {
                      console.log(e)
                        if (e.accNo==useraccNo)
                        {
                          setDetails(e)
                        }

                    })
                    console.log(details)
              }
  return (
          <>
                <div className='text-center text-[50px] shadow-[1px_1px_5px_0px_black]'>Account Details</div>
                <div className=' rounded-[10px] p-10 shadow-[1px_1px_5px_0px_black] m-3 w-[50%] text-center mx-auto'>

                  <table className='mx-auto'>
                    <tbody>
                      <tr> <th className='float-left'>Account No:- {details.accNo}</th></tr>
                      <tr> <th className='float-left'>Name:-       {details.Name}</th></tr>
                      <tr> <th className='float-left'>Balance:-    {details.Balance}</th></tr>
                      <tr> <th className='float-left'>Status:-     {details.Status}</th></tr>
                     
                      
                 
                    </tbody>
                  </table>
                </div>
          
          </>
  );
}

export default App;
