local lastUnlockTime = 0

function runScholarUpdate()
    local currentTime = os.time()
    if currentTime - lastUnlockTime > 60 then  -- 5 minutes in seconds
        lastUnlockTime = currentTime
        hs.execute("/Users/daniilgurgurov/Desktop/projects/scholar_rag/run.sh")
    end
end

caffeinateWatcher = hs.caffeinate.watcher.new(function(eventType)
    if eventType == hs.caffeinate.watcher.screensDidUnlock then
        runScholarUpdate()
    end
end)
caffeinateWatcher:start()