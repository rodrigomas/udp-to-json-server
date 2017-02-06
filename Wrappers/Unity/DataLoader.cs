/**
Created on Nov 21, 2016

@author: Rodrigo Marques Almeida da Silva
*/
using UnityEngine;
using System.Collections;

public class DataLoader : MonoBehaviour
{
	[Range(0.1f,5.0f)]
	public float PoolingInterval = 1.0f;
	
	public string URL = "http://localhost:8000/";
	
	public delegate void DataUpdated(DataMessage message, float t);

    public event DataUpdated OnUpdate = null;
	
	public class DataMessage
    {
        public int ANNAngle = 0;
		public string ANNDir = "D";
		public string MentalDir = "D";
		public int MentalIntensity = 0;		
		public int Acceleration = 0;
		public int Speed = 0;
		public int Temperature = 0;
		public int BMP = 0;
		public int Direction = 0;
		public int Limit = 0;		
		public int TempBody01 = 0;
		public int HumidityBody01 = 0;
		public int TempBody02 = 0;
		public float GPSLat;
		public float GPSLong;
		public float GPSSpeed;
		public float GyroX;
		public float GyroY;
		public float GyroZ;
    }
	
    private DataMessage _Last = null;
    private float _Timer = 0;

	void Start ()
    {
		_Last = new DataMessage();
	}
	
	// Use update to avoid thread creation (only request creates new thread)
	// We can use IOCP
	void Update ()
    {
        _Timer += Time.deltaTime;

        if(_Timer > PoolingInterval)
        {
            MakeRequest();

            _Timer = 0;
        }
	}
    public DataMessage GetData()
    {
        return _Last;
    }

    private void MakeRequest()
    {
        string url = URL;

        WWW www = new WWW(url);

        StartCoroutine(WaitForRequest(www));
    }

    IEnumerator WaitForRequest(WWW www)
    {
        yield return www;

         // Error Check
        if (www.error == null)
        {
            try
            {
                DataMessage Message = JsonUtility.FromJson<DataMessage>(www.text);

                if (Message != null)
                {
                    _Last = Message;
                }
                
                if(OnUpdate != null)
                {
                    OnUpdate(Message, Time.time);
                }
                
            } catch
            {

            }            
        }
        else
        {
            Debug.Log("WWW Error: " + www.error);
        }
    }
}
