function map = push_down (bw, gray, rate)
%% push down low pixels
map = bw;
for i = 2:size (bw,1) -1
    for j = 2:size(bw,2) -1
        if bw(i,j) == 0
            continue
        end
        for x = i-1:i+1
            for y = j-1:j+1
                if gray (x, y) < gray(i,j) * rate;
                    map (x, y) = 0;
                end
            end
        end
    end
end