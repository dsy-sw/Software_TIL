package com.example.weather

import android.content.res.ColorStateList
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.SeekBar
import com.bumptech.glide.Glide
import com.example.mylib.openapi.openweather.OpenWeather
import com.example.mylib.openapi.piapi.PiApi
import com.example.weater.R
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        OpenWeather.getWeatherCast("Seoul"){
            textDescription.text = it.weather[0].description
            val icon = it.weather[0].icon
            val iconPath = "http://openweathermap.org/img/w/${icon}.png"
            Glide.with(this).load(iconPath).into(imgWeather)

            // 온도를 포함해서 기타 정보 출력
            val temp = it.main.temp-273.15
            txtWeatherInfo.text = "온도: ${"%.1f".format(temp)}도, 습도: ${it.main.humidity}"
        }

        ledSwitch.setOnCheckedChangeListener { buttonView, isChecked ->
            if(isChecked){      // switch on
                PiApi.controlLed("1","on") {
                    if (it.result == "OK") {
                        imgLight.imageTintList = ColorStateList.valueOf(Color.YELLOW)
                    }
                }
            } else {        // switch off
                PiApi.controlLed("1", "off") {
                    if (it.result == "OK") {
                        imgLight.imageTintList = ColorStateList.valueOf(Color.DKGRAY)
                    }
                }
            }
        }

        seekAngle.setOnSeekBarChangeListener(object: SeekBar.OnSeekBarChangeListener{
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                PiApi.controlServo("1", progress) {
                    if(it.result == "OK"){
                        txtServo.text = "서보 모터: $progress"
                    }
                }
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {
            }

            override fun onStopTrackingTouch(seekBar: SeekBar?) {
            }
        })
    }
}