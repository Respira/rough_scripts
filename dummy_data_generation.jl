import JSON

type time_res_data
    data::Array{UInt16}
    samp_rate::Int
    time_stamp::DateTime
end

type event_data
    time_of_event::Array{Int}
end

type processed_data
     averages::Dict{String,Float64}
     ranges::Dict{String,Float64}
     time_stamp::DateTime
     measure_duration::Int
end

#Vars
no_set=10;  # The number of seperate datasets
var_1=100;
var_2=10;

####    Generate typical breathing data
# Time resolved data
breath_time=Vector{time_res_data}(no_set);
for set in 1:no_set
    breath_time[set]=time_res_data(rand(Array{UInt16}(1:1e3),var_1),8000,now())
end
# Event data
breath_event=Vector{event_data}(no_set);
for set in 1:no_set
    breath_event[set]=event_data(cumsum((rand(Array{Int}(1:20),var_2))))
end
# Processed data
breath_processed=Vector{processed_data}(no_set);
for set in 1:no_set
    breath_processed[set]=processed_data(Dict("frequency" => rand(),"depth" => rand(),"rise_time" => rand(),"fall_time" => rand()),Dict("frequency_max" => rand(),"depth_max" => rand(),"rise_time_max" => rand(),"fall_time_max" => rand(),"frequency_min" => rand(),"depth_min" => rand(),"rise_time_min" => rand()),now(),30)
end

####    Generate typical heart data
# Time resolved data
heart_time=Vector{time_res_data}(no_set);
for set in 1:no_set
    heart_time[set]=time_res_data(rand(Array{UInt16}(1:1e3),var_1),8000,now())
end
# event data
heart_event=Vector{event_data}(no_set);
for set in 1:no_set
    heart_event[set]=event_data(cumsum((rand(Array{Int}(1:20),var_2))))
end
# Processed data
heart_processed=Vector{processed_data}(no_set);
for set in 1:no_set
    heart_processed[set]=processed_data(Dict("frequency" => rand()),Dict("frequency_max" => rand(),"frequency_min" => rand()),now(),30)
end

####    Generate typical accelerometer data
# Time resolved data
acc_time=Vector{time_res_data}(no_set);
for set in 1:no_set
    acc_time[set]=time_res_data(rand(Array{UInt16}(1:1e3),3,var_2),3200,now())
end

####    Generate typical audio data
# Time resolved data
audio_time=Vector{time_res_data}(no_set);
for set in 1:no_set
    audio_time[set]=time_res_data(rand(Array{UInt16}(1:1e3),4,var_1),44100,now())
end
# event data
syllable_event=Vector{event_data}(no_set);
for set in 1:no_set
    syllable_event[set]=event_data(cumsum((rand(Array{Int}(1:20),var_2))))
end

####    Generate typical stuttering data
stutter_event=Vector{event_data}(no_set);
for set in 1:no_set
    stutter_event[set]=event_data(cumsum((rand(Array{Int}(1:20),var_2))))
end
# Processed data
stutter_processed=Vector{processed_data}(no_set);
for set in 1:no_set
    stutter_processed[set]=processed_data(Dict("stutter_occurance" => round(rand())),Dict("stutter_occurance_max" => round(rand()),"stutter_occurance_min" => round(rand())),now(),30)
end


data_dict=Dict("breath_time" => breath_time,"breath_event" => breath_event,"breath_processed" => breath_processed,"heart_time" => heart_time,"heart_event" => heart_event,"heart_processed" => heart_processed, "audio_time" => acc_time,"audio_time" => audio_time,"syllable_event" => syllable_event,"stutter_event" => stutter_event, "stutter_processed" => stutter_processed);
jsonstring=JSON.json(data_dict);
open("date_user_0001.json", "w") do f
        write(f, jsonstring)
end
